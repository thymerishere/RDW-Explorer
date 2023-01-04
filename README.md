# RDW-Explorer

Used for exploring the [Open Data RDW](https://opendata.rdw.nl) repository from the dutch government containing public data on registered vehicles.

## Current Functions
- Search for vehicles based on partial information and partial plate information
- Combines information of both the 'Gekentekende Voertuigen' dataset with the 'Gekentekende Voertuigen Brandstof' dataset
- Simple command line interface

## Getting Started
1. Download the repository
2. Install with `pip install .`
3. Run with `python main.py --kenteken S____3 --merk FERRARI` (All Ferraris with plates starting with 'S' and ending with '3')

## Supported tags
- Kenteken (plate): `-k`, `--kenteken`
- Merk (brand): `-m`, `--merk`
- Handelsbenaming (model): `-o`, `--handelsbenaming`
