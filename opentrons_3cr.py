from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Opentrons_3CR",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for 3CR',
    'apiLevel': '2.12'
}


# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    source_plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', location='4', label='Source_Plate')
    destination_plate_1 = protocol.load_labware('sarstedt_96_wellplate_200ul', location='1', label='Destination_Plate_1')
    destination_plate_2 = protocol.load_labware('sarstedt_96_wellplate_200ul', location='2', label='Destination_Plate_2')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', location='7', label='Tip_Rack_1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', location='8', label='Tip_Rack_2')
    tiprack_3 = protocol.load_labware('opentrons_96_tiprack_300ul', location='9', label='Tip_Rack_3')
    # pipette
    right_pipette = protocol.load_instrument('p300_single', mount='right', tip_racks=[tiprack_1, tiprack_2, tiprack_3])







