# Auto-generated. Do not edit by hand.
from __future__ import annotations

from typing import Optional, Literal
from bwEDI.segment import Segment, element, id_element
from bwEDI.x12_types import X12ID, X12Nn, X12R


class AT3(Segment):
    """
    AT3 - Bill of Lading Rates and Charges
    
    Description:
        To specify Bill of Lading rates and charges
    
    Source:
        https://www.kasoftware.com/schema/edi/x12/00501/segments/AT3/
    """
    _id: Literal["AT3"] = id_element(name="AT3")

    AmountCharged: X12Nn = element(
        name="AT301",
        description="Amount Charged",
        mandatory=True,
        min_length=1,
        max_length=15,
    )

    FreightRateQualifier: Optional[X12ID] = element(
        name="AT302",
        description="Freight Rate Qualifier",
        min_length=2,
        max_length=2,
    )

    FreightRate: Optional[X12R] = element(
        name="AT303",
        description="Freight Rate",
        min_length=1,
        max_length=9,
    )

    RatedAsQualifier: Optional[X12ID] = element(
        name="AT304",
        description="Rated-as Qualifier",
        min_length=2,
        max_length=2,
    )

    Quantity: Optional[X12R] = element(
        name="AT305",
        description="Quantity",
        min_length=1,
        max_length=15,
    )

    BillOfLadingChargeCode: Optional[X12ID] = element(
        name="AT306",
        description="Bill of Lading Charge Code",
        min_length=3,
        max_length=3,
    )

    PercentageAsDecimal: Optional[X12R] = element(
        name="AT307",
        description="Percentage as Decimal",
        min_length=1,
        max_length=10,
    )
