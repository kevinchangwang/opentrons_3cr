from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "Organic Phase mixing",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for organic phase mixing',
    'apiLevel': '2.12'
}

ionizable_lipid_amount = 2
lipid_master_mix_amount = 12
organic_phase_amount = 10
aqueous_phase_amount = 20

tip_rack_1_location = '10'
tip_rack_2_location = '7'
tip_rack_3_location = '4'
tip_rack_4_location = '1'

master_mix_source_plate_location = '10'
master_mix_col = '1'
ionizable_lipid_source_plate_location = '7'
organic_phase_plate_location = '11'



def run(protocol: protocol_api.ProtocolContext):
    # Load Labware
    master_mix_source_plate = protocol.load_labware('pcr_96_wellpate_singlep20', location=master_mix_source_plate_location,
                                         label='Master_Mix_Source_Plate')
    ionizable_lipid_source_plate = protocol.load_labware('sarstedt_96_wellplate_200ul', location=ionizable_lipid_source_plate_location, label='Ionizable_Lipid_Plate')
    organic_phase_plate = protocol.load_labware('pcr_96_wellpate_singlep20', location=organic_phase_plate_location,
                                              label='Organic_Phase_Destination_Plate')
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', location=tip_rack_1_location, label='Tip_Rack_1')
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', location=tip_rack_2_location, label='Tip_Rack_2')
    tiprack_3 = protocol.load_labware('opentrons_96_tiprack_20ul', location=tip_rack_2_location, label='Tip_Rack_2')
    tiprack_4 = protocol.load_labware('opentrons_96_tiprack_300ul', location=tip_rack_4_location, label='')
    # Load Pipettes
    p20_multi_pipette = protocol.load_instrument('p20_multi_gen2', mount='left',
                                                 tip_racks=[tiprack_1,tiprack_2, tiprack_3])
    p300_multi_pipette = protocol.load_instrument('p300_multi_gen2', mount='right',tip_racks=[tiprack_4])
    #Add master mix to empty PCR plate
    p20_multi_pipette.transfer(lipid_master_mix_amount, master_mix_source_plate.columns_by_name()[master_mix_col], organic_phase_plate.wells(), new_tip='never')

    #Add ionizable lipid to PCR plate and mix
    p20_multi_pipette.transfer(ionizable_lipid_amount, ionizable_lipid_source_plate.wells(), organic_phase_plate.wells, new_tip='always', mix_after=(3,(ionizable_lipid_amount + lipid_master_mix_amount)/2))

    #Formulate nanoparticle
    p20_multi_pipette.

