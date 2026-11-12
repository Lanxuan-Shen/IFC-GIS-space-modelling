"""Report the legal-physical associations encoded in Model_V1.0.6.ifc.

Reproduces the counts reported in Section 6.3 of the paper.
Usage: python verify_associations.py Model_V1.0.6.ifc
"""
import sys
import ifcopenshell

model = ifcopenshell.open(sys.argv[1] if len(sys.argv) > 1 else "Model_V1.0.6.ifc")
print("Schema:", model.schema)

zones = model.by_type("IfcSpatialZone")
rings = [e for e in model.by_type("IfcBuiltElement") if e.ObjectType == "TunnelRing"]
print(f"IfcSpatialZone instances: {len(zones)}")
print(f"Tunnel rings (IfcBuiltElement, ObjectType=TunnelRing): {len(rings)}")

refs = {}
for z in zones:
    related = set()
    for rel in model.by_type("IfcRelReferencedInSpatialStructure"):
        if rel.RelatingStructure == z:
            related |= {e.id() for e in rel.RelatedElements}
    refs[z.ObjectType] = related
    print(f"  {z.ObjectType:<16} #{z.id():<6} GlobalId={z.GlobalId}  referenced rings: {len(related)}")

c, e, d = refs.get("CROWN_PARCEL", set()), refs.get("EASEMENT", set()), refs.get("DEPTHLIMITATION", set())
print(f"Rings shared by CROWN_PARCEL and DEPTHLIMITATION: {len(c & d)}")
print(f"EASEMENT rings also referenced by CROWN_PARCEL: {len(e & c)} of {len(e)}")
