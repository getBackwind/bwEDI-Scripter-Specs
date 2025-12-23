# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12AN, X12ID, X12Nn


class L5(Segment):
    """
    L5 - Description, Marks and Numbers
    
    Description:
        To specify the line item in terms of description, quantity, packaging, and marks and numbers
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00401/segments/L5/
    """
    _id: Literal["L5"] = id_element(name="L5")

    LadingLineItemNumber: Optional[X12Nn] = element(
        name="L501",
        description="Lading Line Item Number",
        min_length=1,
        max_length=3,
    )

    LadingDescription: Optional[X12AN] = element(
        name="L502",
        description="Lading Description",
        min_length=1,
        max_length=50,
    )

    CommodityCode: Optional[X12AN] = element(
        name="L503",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CommodityCodeQualifier: Optional[X12ID] = element(
        name="L504",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    PackagingCode: Optional[X12AN] = element(
        name="L505",
        description="Packaging Code",
        min_length=3,
        max_length=5,
    )

    MarksAndNumbers: Optional[X12AN] = element(
        name="L506",
        description="Marks and Numbers",
        min_length=1,
        max_length=48,
    )

    MarksAndNumbersQualifier: Optional[X12ID] = element(
        name="L507",
        description="Marks and Numbers Qualifier",
        min_length=1,
        max_length=2,
    )

    CommodityCodeQualifier2: Optional[X12ID] = element(
        name="L508",
        description="Commodity Code Qualifier",
        min_length=1,
        max_length=1,
    )

    CommodityCode2: Optional[X12AN] = element(
        name="L509",
        description="Commodity Code",
        min_length=1,
        max_length=30,
    )

    CompartmentIDCode: Optional[X12ID] = element(
        name="L510",
        description="Compartment ID Code",
        min_length=1,
        max_length=1,
    )
