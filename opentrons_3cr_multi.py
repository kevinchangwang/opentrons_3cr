from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Opentrons_3CR_multi",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for 3CR',
    'apiLevel': '2.12'
}

# This protocol will use the Opentrons OT-2 robot to combine the 3 components for the 3 component reaction
# Version: Multi-channel pipette and single-channel pipette

# Set the component volume here
component_volume = 40

# Change the location of the plates here
headgroup_source_plate_location = '8'
linker_source_plate_location = '7'
tail_source_plate_location = '10'
destination_plate_location = '11'

# This protocol requires 3 pipette racks, 1 for each component. Indicate the locations here
tip_rack_1_location = '4'
tip_rack_2_location = '5'
tip_rack_3_location = '6'

# Specifies the transfer of A components from the source plate well to destination plate rows
A_Component_Dict = {
    'A1': 'A',
    'B1': 'B',
    'C1': 'C',
    'D1': 'D',
    'A2': 'E',
    'B2': 'F',
    'B3': 'G',
    'B4': 'H'
}

# Specifies the transfer of C components from the source plate well to destination plate columns
C_Component_Dict = {
    'A4': '1',
    'B4': '2',
    'C4': '3',
    'D4': '4',
    'A5': '5',
    'B5': '6',
    'C5': '7',
    'D5': '8',
    'A6': '9',
    'B6': '10',
    'C6': '11',
    'D6': '12'
}


# protocol run function
def run(protocol: protocol_api.ProtocolContext):
    # labware
    source_plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', location='4',
                                         label='Source_Plate')
    destination_plate = protocol.load_labware('sarstedt_96_wellplate_200ul', location='11',
                                              label='Destination_Plate')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_1_location, label='Tip_Rack_1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_2_location, label='Tip_Rack_2')
    tiprack_3 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_3_location, label='Tip_Rack_3')
    # pipette
    right_pipette = protocol.load_instrument('p300_single_gen2', mount='right',
                                             tip_racks=[tiprack_1, tiprack_2, tiprack_3])
    left_pipette = protocol.load_instrument('p300_multi_gen2', mount='right',
                                             tip_racks=[tiprack_1, tiprack_2, tiprack_3])

    # distribute B components to an empty plate
    left_pipette.transfer(component_volume, source_plate.wells('C3', 'C4'), destination_plate.wells(),
                           new_tip='never')

    # distribute A components to the designated rows
    for component in A_Component_Dict:
        right_pipette.transfer(component_volume, source_plate.wells_by_name()[component],
                               destination_plate.rows_by_name()[A_Component_Dict[component]], new_tip='always')

    # distribute C components to the designated columns
    for component in C_Component_Dict:
        left_pipette.transfer(component_volume, source_plate.wells_by_name()[component],
                               destination_plate.columns_by_name()[C_Component_Dict[component]], new_tip='always')
