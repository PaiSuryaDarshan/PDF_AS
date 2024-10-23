import selfies as sf

import selfies as sf

benzene = "C12CCCCC1CCC2"

# SMILES -> SELFIES -> SMILES translation
try:
    benzene_sf = sf.encoder(benzene)  # [C][=C][C][=C][C][=C][Ring1][=Branch1]
    benzene_smi = sf.decoder(benzene_sf)  # C1=CC=CC=C1
except sf.EncoderError:
    pass  # sf.encoder error!
except sf.DecoderError:
    pass  # sf.decoder error!

len_benzene = sf.len_selfies(benzene_sf)  # 8

symbols_benzene = list(sf.split_selfies(benzene_sf))
# ['[C]', '[=C]', '[C]', '[=C]', '[C]', '[=C]', '[Ring1]', '[=Branch1]']

print(benzene_sf)
print(benzene_smi)