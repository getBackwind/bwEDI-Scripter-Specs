from typing import Optional, Literal, Any

# === Base helpers ===

class Segment:
    """
    Base class for all X12 segments.
    Each subclass defines attributes using element() or id_element().
    """
    _id: str  # segment ID literal, e.g. "AAA"
    def __init__(self, **kwargs: Any): ...
    def to_dict(self) -> dict: ...
    def __repr__(self): ...

# === Element declarations ===

def id_element(name: str) -> Literal[str]:
    """Declare the fixed ID element of a segment (e.g. 'AAA')."""
    return name

def element(
    *,
    name: str,
    description: str = "",
    mandatory: bool = False,
    min_length: int = 0,
    max_length: int = 0,
) -> Any:
    """Define a data element in a segment."""
    ...

# === Common datatypes ===

class X12ID(str): """Identifier (e.g. codes, qualifiers)."""
class X12AN(str): """Alphanumeric."""
class X12DT(str): """Date."""
class X12TM(str): """Time."""
class X12N(float): """Numeric."""
class X12R(float): """Decimal / real number."""

# === Optional type helper ===
# (Used for fields that can be None)
OptionalField = Optional

# === Example pattern ===
#
# class AAA(Segment):
#     _id: Literal["AAA"] = id_element(name="AAA")
#     YesNoConditionOrResponseCode: X12ID = element(
#         name="AAA01", description="Yes/No Condition or Response Code", mandatory=True, min_length=1, max_length=1)
#     AgencyQualifierCode: Optional[X12ID] = element(
#         name="AAA02", description="Agency Qualifier Code", min_length=2, max_length=2)


# === Document Configuration ===

class DocumentConfiguration:
    """
    Holds EDI delimiters and metadata for document generation.
    """
    def __init__(
        self,
        version: str = "004010",
        element_separator: str = "*",
        segment_terminator: str = "~",
        sub_element_separator: str = ">",
        include_trailing_separators: bool = False,
    ):
        self.version = version
        self.element_separator = element_separator
        self.segment_terminator = segment_terminator
        self.sub_element_separator = sub_element_separator
        self.include_trailing_separators = include_trailing_separators

    def to_dict(self) -> dict:
        """Return configuration as a serializable dict."""
        return {
            "version": self.version,
            "element_separator": self.element_separator,
            "segment_terminator": self.segment_terminator,
            "sub_element_separator": self.sub_element_separator,
            "include_trailing_separators": self.include_trailing_separators,
        }

# Default config used for most EDI builds
DOCUMENT_CONFIG_DEFAULT = DocumentConfiguration()


# === Flat Envelope Header (ISA/GS/ST summary) ===

class EdiFlatHeader:
    """
    Basic metadata for an interchange and functional group.
    Used to populate ISA/GS/ST headers and control values.
    """
    SenderIdQualifier: str
    SenderID: str
    ReceiverIdQualifier: str
    ReceiverID: str
    InterchangeID: str  # 9-digit control number
    Date: str           # YYYYMMDD
    Time: str           # HHMM
    AuthorizationQualifier: str = "00"
    AuthorizationNumber: str = "          "  # 10 spaces
    SecurityQualifier: str = "00"
    SecurityNumber: str = "          "
    ControlStandardID: str = "U"
    Acknowledgment: str = "0"
    UsageIndicator: str = "P"  # P = Production, T = Test
    DocumentType: str          # e.g., "850", "997", "855"
    FunctionalIdCode: str      # e.g., "SH", "IN"
    AgencyCode: str = "X"
    GroupID: str | None = None
    TransactionSetID: str | None = None
