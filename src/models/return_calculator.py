#%%
from pydantic import BaseModel, Field 
import typing 
import math

class ReturnCalculator(BaseModel):
    monthly_amount: int = Field(gt=0, le=1000000)
    annual_return: float = Field(ge=0, le=100)
    tenure_in_months: int = Field(gt=0, le=540)
    is_compounded: bool = Field(default=1)
    
    def get_total_investment_amount(self) -> int:
        monthly_return = self.annual_return/12/100
        if self.is_compounded:
            multipler = ((((1+monthly_return)**self.tenure_in_months) - 1)* (1+monthly_return))/monthly_return
            # (1+ (monthly_return**self.tenure_in_months)-1)/monthly_return
            # ((((1 + MR)**(M))-1) * (1 + MR))/MR
        else:
            multipler = (1+ (monthly_return*self.tenure_in_months))
        return round(multipler * self.monthly_amount, 0)
    
    def get_invested_amount(self):
        return self.tenure_in_months*self.monthly_amount
        
class SIPCalculator(ReturnCalculator):
    def get_return_amount(self) -> dict:
        invested_amount = super().get_invested_amount()
        total_amount = super().get_total_investment_amount()
        return_pct = round((total_amount-invested_amount)*100/invested_amount, 2)
        annualised_returns = round(return_pct/(self.tenure_in_months/12), 2)
        return {
            "monthly_amount": self.monthly_amount,
            "invested_amount": invested_amount,
            "total_amount": total_amount,
            "return_amount": total_amount - invested_amount,
            "return_pct": return_pct, 
            "annualised_returns": annualised_returns
        }
# %%
# sip_1 = SIPCalculator(monthly_amount=300, tenure_in_months= 2, annual_return= 10)
# print(sip_1.get_return_amount())