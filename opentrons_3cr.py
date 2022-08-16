from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Opentrons_3CR",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for 3CR',
    'apiLevel': '2.12'
}

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
    solvent_plate = protocol.load_labware('usascientific_12_reservoir_22ml', location='5',
                                          label='Solvent_Plate')
    source_plate = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', location='4',
                                         label='Source_Plate')
    destination_plate = protocol.load_labware('sarstedt_96_wellplate_200ul', location='1',
                                              label='Destination_Plate_1')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_300ul', location='7', label='Tip_Rack_1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_300ul', location='8', label='Tip_Rack_2')
    tiprack_3 = protocol.load_labware('opentrons_96_tiprack_300ul', location='9', label='Tip_Rack_3')
    tiprack_4 = protocol.load_labware('opentrons_96_tiprack_300ul', location='10', label='Tip_Rack_4')
    # pipette
    right_pipette = protocol.load_instrument('p300_single_gen2', mount='right',
                                             tip_racks=[tiprack_1, tiprack_2, tiprack_3])
    left_pipette = protocol.load_instrument('p300_multi_gen2', mount='left',
                                            tip_racks=[tiprack_4])
    # transfer 57.5ul of solvent to both destination plates
    left_pipette.pick_up_tip()
    left_pipette.distribute(57.5, solvent_plate.well('A1'), destination_plate.wells(), new_tip='never')
    left_pipette.drop_tip()

    # distribute A components to the designated rows
    right_pipette.pick_up_tip()
    for component in A_Component_Dict:
        right_pipette.transfer(20, source_plate.wells_by_name()[component],
                               destination_plate.rows_by_name()[A_Component_Dict[component]], new_tip='always')

    # distribute B components to the designated plates
    right_pipette.transfer(20, source_plate.wells_by_name()['C3'], destination_plate.wells(), new_tip='always')

    # distribute C components to the designated columns
    for component in C_Component_Dict:
        right_pipette.transfer(20, source_plate.wells_by_name()[component],
                               destination_plate.columns_by_name()[A_Component_Dict[component]], new_tip='always')

    right_pipette.drop_tip()
