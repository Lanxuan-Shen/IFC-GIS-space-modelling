# IFC-GIS-space-modelling

Files supporting the prototype implementation reported in:

Shen, L., Atazadeh, B., Ho, S., & Rajabifard, A. *Extending IFC for 3D Land and Property Data Management in Underground Infrastructure Projects*. Transactions in GIS (under review).

## Repository contents

| Path | Description |
|---|---|
| `Model_V1.0.6.ifc` | IFC file examined in Section 6 of the paper (schema IFC4X3_ADD2). |
| `scripts/verify_associations.py` | Python script that extracts the legal–physical associations in `Model_V1.0.6.ifc` and reproduces the counts reported in Section 6.3. |
| `GIS/` | QGIS project and layers used for the GIS views (Figures 8a and 9). |
| `validation/` | buildingSMART Validation Service report for `Model_V1.0.6.ifc`. |

SHA-256 of `Model_V1.0.6.ifc`: `f0e5c315368b68a9520e3b80123d0aedf4c8c2d465fb64b32eb0fac043c217b9`

## The IFC file

- **Legal spaces:** five `IfcSpatialZone` instances with `PredefinedType = USERDEFINED` and `ObjectType` = `LOT`, `RESERVE`, `CROWN_PARCEL`, `EASEMENT` or `DEPTHLIMITATION`. Legal attributes are stored in the custom property sets `LegalZoneCommon`, `CrownParcelRef`, `LegalEasement` and `LegalVertical`.
- **Physical elements:** 798 tunnel rings (`IfcBuiltElement`, `ObjectType = TunnelRing`).
- **Legal–physical associations:** three `IfcRelReferencedInSpatialStructure` relationships (#115251–#115253) reference 174 rings from `CROWN_PARCEL`, 15 from `EASEMENT` and 40 from `DEPTHLIMITATION`. `LOT` and `RESERVE` have no ring associations.
- **Georeferencing:** `IfcProjectedCRS` (GDA94 / MGA zone 55, EPSG:28355; AHD) with `IfcMapConversion`.
- The file was exported from Autodesk Revit and also contains 32 `IfcSpace` instances (`LongName = Room`) from the Revit model. They are not part of the legal-space configuration and are not referenced by the legal–physical relationships.

## Validation and inspection

- The file was checked with the buildingSMART Validation Service in November 2026 (report in `validation/`). It was reported Valid for STEP syntax, IFC schema, normative IFC rules and industry practices. The report header also displayed a warning alongside the MVD declarations CoordinationView and QuantityTakeOffAddOnView.
- The file was opened in BIMvision 3.1.2 and Solibri 25.12.0.83. In both viewers, the five legal-space instances could be located, and their IfcSpatialZone entity type, ObjectType values and populated property sets were accessible. Legal–physical associations were not retrieved through either viewer's interface; they can be inspected in the STEP text (#115251–#115253) or with `scripts/verify_associations.py`:

```
python scripts/verify_associations.py Model_V1.0.6.ifc
```

## Requirements

- Python 3 with IfcOpenShell (`verify_associations.py` was tested with IfcOpenShell 0.9.0)
- QGIS 4.0.1 for the GIS project

## Not included

The source survey plans (Original Plans), the Revit model and the IfcOpenShell post-processing scripts used to create the IFC file are not redistributed. The remaining data supporting the findings of the study are available from the corresponding author upon reasonable request.

## Licence and data sources

- Unless otherwise stated, files in this repository are released under the MIT License (see `LICENSE`).
- Vicmap layers in `GIS/` are © State of Victoria (Department of Transport and Planning) and are used under the Creative Commons Attribution 4.0 International licence. Other third-party layers retain their providers' licences and attribution requirements.

## Citation

If you use these materials, please cite the paper above and this repository.
