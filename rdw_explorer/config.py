from dataclasses import dataclass

@dataclass
class Config:
    
    gekentekende_voertuigen_api = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

    gekentekende_voertuigen_brandstof_api = "https://opendata.rdw.nl/Voertuigen/Open-Data-RDW-Gekentekende_voertuigen_brandstof/8ys7-d773"

    fields_name_in_headers: str = "X-SODA2-Fields"

    types_name_in_headers: str = "X-SODA2-Types"
