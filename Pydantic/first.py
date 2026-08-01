from typing import List, Optional , Dict  , Annotated
from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator , model_validator , computed_field

class Address(BaseModel) :
    city : str 
    state : str 
    pin : int 



class PatientData(BaseModel) :
    name : Annotated[str , Field(title="Enter name" , description="Enter your official name" , examples=["Daksh" , "Hello"])] 
    full_name : str = Field(max_length=50) 
    email : EmailStr 
    weight : int 
    height : int 
    url   : AnyUrl
    address : Address
    age : int = Field(gt=0 , lt=100)
    allergies  : Optional[List[str]] = None 
    contact_info : Dict[str , str] 


    @computed_field
    @property
    def bmi(self) -> float :
        bmi = round(self.weight / (self.height**2) , 2 )
        return bmi 

    @model_validator(mode= 'after')
    @classmethod
    def emergency_details_validator(cls , model) :
        if (model.age > 60 and 'emergency' not in  model.contact_info) :
            raise ValueError('Emergency contact must be present for patients above 60 ')

        return model 

    @field_validator('email')
    @classmethod
    def email_validator(cls , value) :
        valid_domains = ['hdfc.com' , 'gmail.com'] 
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains :
            raise ValueError('Domain not in valid domain list .. ')

        return value 

    @field_validator('name')
    @classmethod
    def name_transform(cls , value) :
        return value.upper() ; 


def add_patient(patient : PatientData) :
    print(patient.name)
    print(patient.age)

def update_patient(patient : PatientData) : 
    print(patient.name)
    print(patient.age)    


patient_1 = {"name" : "Daksh" , "age" : 25 , }



patient = PatientData(name="Daksh" , full_name="Daksh Mane " , age=15 , weight=45 , height=150 , url="https://youtube.com" , email="daksh@gmail.com" , address={"city": "Ahmedabad" , "pin": 35454 , "state": "Gujarat"} , contact_info={"phone" : "6354757812"} )

temp = patient.model_dump()
print(temp)

