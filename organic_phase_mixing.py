from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Organic Phase mixing",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for organic phase mixing',
    'apiLevel': '2.12'
}

ionizable_lipid_amount = 2
lipid_mastermix_amount = 12

def run(protocol: protocol_api.ProtocolContext):
    # Load Labware
    source_plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', location='4',
                                         label='Source_Plate')
    destination_plate = protocol.load_labware('sarstedt_96_wellplate_200ul', location='11',
                                              label='Destination_Plate')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_1_location, label='Tip_Rack_1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_2_location, label='Tip_Rack_2')
    tiprack_3 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_3_location, label='Tip_Rack_3')
    # Load Pipettes
    left_pipette = protocol.load_instrument('p20_multi_gen2', mount='left',
                                            tip_racks=[tiprack_1, tiprack_2, tiprack_3])



