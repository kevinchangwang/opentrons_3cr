from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': "formulation_mixing",
    'author': 'Kevin <kevinchang.wang@mail.utoronto.ca',
    'description': 'Opentrons liquid dispensing protocol for 3CR',
    'apiLevel': '2.12'
}

# This protocol will use the Opentrons OT-2 robot to mix the aqueous phase containing mRNA with the organic phase