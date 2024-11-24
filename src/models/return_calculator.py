#%%
from pydantic import BaseModel, Field 
import typing 

class ReturnCalculator(BaseModel):
    monthly_amount: int = Field(gt=0, le=1000000)
    annual_return: float = Field(ge=0, le=100)
    tenure_in_years: int = Field(gt=0, le=50)
    is_compounded: bool = Field(default=1)
    
    def get_return_amount(self) -> int:
        if self.is_compounded:
            return 100
        else:
            return 10
        
class SIPCalculator(ReturnCalculator):
    def get_return_amount(self):
        return {
            "monthly_amount": self.monthly_amount,
            "return_amount": super().get_return_amount()
        }
# %%
sip_1 = SIPCalculator(monthly_amount=300, tenure_in_years= 2, annual_return= 10)
print(sip_1.get_return_amount())