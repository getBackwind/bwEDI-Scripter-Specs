# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12R


class HI(Segment):
    """
    HI - Health Care Information Codes
    
    Description:
        To supply information related to the delivery of health care
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/HI/
    """
    _id: Literal["HI"] = id_element(name="HI")

    CodeListQualifierCode: X12ID = element(
        name="HI0101",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode: X12AN = element(
        name="HI0102",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier: Optional[X12ID] = element(
        name="HI0103",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod: Optional[X12AN] = element(
        name="HI0104",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount: Optional[X12R] = element(
        name="HI0105",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity: Optional[X12R] = element(
        name="HI0106",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier: Optional[X12AN] = element(
        name="HI0107",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode2: Optional[X12AN] = element(
        name="HI0108",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode: Optional[X12ID] = element(
        name="HI0109",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode2: X12ID = element(
        name="HI0201",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode3: X12AN = element(
        name="HI0202",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier2: Optional[X12ID] = element(
        name="HI0203",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod2: Optional[X12AN] = element(
        name="HI0204",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount2: Optional[X12R] = element(
        name="HI0205",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity2: Optional[X12R] = element(
        name="HI0206",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier2: Optional[X12AN] = element(
        name="HI0207",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode4: Optional[X12AN] = element(
        name="HI0208",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode2: Optional[X12ID] = element(
        name="HI0209",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode3: X12ID = element(
        name="HI0301",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode5: X12AN = element(
        name="HI0302",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier3: Optional[X12ID] = element(
        name="HI0303",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod3: Optional[X12AN] = element(
        name="HI0304",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount3: Optional[X12R] = element(
        name="HI0305",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity3: Optional[X12R] = element(
        name="HI0306",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier3: Optional[X12AN] = element(
        name="HI0307",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode6: Optional[X12AN] = element(
        name="HI0308",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode3: Optional[X12ID] = element(
        name="HI0309",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode4: X12ID = element(
        name="HI0401",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode7: X12AN = element(
        name="HI0402",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier4: Optional[X12ID] = element(
        name="HI0403",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod4: Optional[X12AN] = element(
        name="HI0404",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount4: Optional[X12R] = element(
        name="HI0405",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity4: Optional[X12R] = element(
        name="HI0406",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier4: Optional[X12AN] = element(
        name="HI0407",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode8: Optional[X12AN] = element(
        name="HI0408",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode4: Optional[X12ID] = element(
        name="HI0409",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode5: X12ID = element(
        name="HI0501",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode9: X12AN = element(
        name="HI0502",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier5: Optional[X12ID] = element(
        name="HI0503",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod5: Optional[X12AN] = element(
        name="HI0504",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount5: Optional[X12R] = element(
        name="HI0505",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity5: Optional[X12R] = element(
        name="HI0506",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier5: Optional[X12AN] = element(
        name="HI0507",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode10: Optional[X12AN] = element(
        name="HI0508",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode5: Optional[X12ID] = element(
        name="HI0509",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode6: X12ID = element(
        name="HI0601",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode11: X12AN = element(
        name="HI0602",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier6: Optional[X12ID] = element(
        name="HI0603",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod6: Optional[X12AN] = element(
        name="HI0604",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount6: Optional[X12R] = element(
        name="HI0605",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity6: Optional[X12R] = element(
        name="HI0606",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier6: Optional[X12AN] = element(
        name="HI0607",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode12: Optional[X12AN] = element(
        name="HI0608",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode6: Optional[X12ID] = element(
        name="HI0609",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode7: X12ID = element(
        name="HI0701",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode13: X12AN = element(
        name="HI0702",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier7: Optional[X12ID] = element(
        name="HI0703",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod7: Optional[X12AN] = element(
        name="HI0704",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount7: Optional[X12R] = element(
        name="HI0705",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity7: Optional[X12R] = element(
        name="HI0706",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier7: Optional[X12AN] = element(
        name="HI0707",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode14: Optional[X12AN] = element(
        name="HI0708",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode7: Optional[X12ID] = element(
        name="HI0709",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode8: X12ID = element(
        name="HI0801",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode15: X12AN = element(
        name="HI0802",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier8: Optional[X12ID] = element(
        name="HI0803",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod8: Optional[X12AN] = element(
        name="HI0804",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount8: Optional[X12R] = element(
        name="HI0805",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity8: Optional[X12R] = element(
        name="HI0806",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier8: Optional[X12AN] = element(
        name="HI0807",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode16: Optional[X12AN] = element(
        name="HI0808",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode8: Optional[X12ID] = element(
        name="HI0809",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode9: X12ID = element(
        name="HI0901",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode17: X12AN = element(
        name="HI0902",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier9: Optional[X12ID] = element(
        name="HI0903",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod9: Optional[X12AN] = element(
        name="HI0904",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount9: Optional[X12R] = element(
        name="HI0905",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity9: Optional[X12R] = element(
        name="HI0906",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier9: Optional[X12AN] = element(
        name="HI0907",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode18: Optional[X12AN] = element(
        name="HI0908",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode9: Optional[X12ID] = element(
        name="HI0909",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode10: X12ID = element(
        name="HI1001",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode19: X12AN = element(
        name="HI1002",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier10: Optional[X12ID] = element(
        name="HI1003",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod10: Optional[X12AN] = element(
        name="HI1004",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount10: Optional[X12R] = element(
        name="HI1005",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity10: Optional[X12R] = element(
        name="HI1006",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier10: Optional[X12AN] = element(
        name="HI1007",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode20: Optional[X12AN] = element(
        name="HI1008",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode10: Optional[X12ID] = element(
        name="HI1009",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode11: X12ID = element(
        name="HI1101",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode21: X12AN = element(
        name="HI1102",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier11: Optional[X12ID] = element(
        name="HI1103",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod11: Optional[X12AN] = element(
        name="HI1104",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount11: Optional[X12R] = element(
        name="HI1105",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity11: Optional[X12R] = element(
        name="HI1106",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier11: Optional[X12AN] = element(
        name="HI1107",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode22: Optional[X12AN] = element(
        name="HI1108",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode11: Optional[X12ID] = element(
        name="HI1109",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )

    CodeListQualifierCode12: X12ID = element(
        name="HI1201",
        description="Code List Qualifier Code",
        mandatory=True,
        min_length=1,
        max_length=3,
    )

    IndustryCode23: X12AN = element(
        name="HI1202",
        description="Industry Code",
        mandatory=True,
        min_length=0,
        max_length=30,
    )

    DateTimePeriodFormatQualifier12: Optional[X12ID] = element(
        name="HI1203",
        description="Date Time Period Format Qualifier",
        min_length=2,
        max_length=3,
    )

    DateTimePeriod12: Optional[X12AN] = element(
        name="HI1204",
        description="Date Time Period",
        min_length=1,
        max_length=35,
    )

    MonetaryAmount12: Optional[X12R] = element(
        name="HI1205",
        description="Monetary Amount",
        min_length=1,
        max_length=18,
    )

    Quantity12: Optional[X12R] = element(
        name="HI1206",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    VersionIdentifier12: Optional[X12AN] = element(
        name="HI1207",
        description="Version Identifier",
        min_length=1,
        max_length=30,
    )

    IndustryCode24: Optional[X12AN] = element(
        name="HI1208",
        description="Industry Code",
        min_length=1,
        max_length=30,
    )

    YesNoConditionOrResponseCode12: Optional[X12ID] = element(
        name="HI1209",
        description="Yes/No Condition or Response Code",
        min_length=1,
        max_length=1,
    )
