from pydantic import BaseModel

class HousingContract(BaseModel):
    """Model showing number of units in a project for various levels of affordability."""
    Contract_ID: int
    Project_ID: int
    PSH_Units: int
    MFI_20: int
    MFI_30: int
    MFI_40: int
    MFI_50: int
    MFI_60: int
    MFI_65: int
    MFI_70: int
    MFI_80: int
    MFI_100: int
    MFI_120: int
