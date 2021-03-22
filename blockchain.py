from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink..", ["Satoshi sent 1 BTC to Ivan",
													"Satoshi sent 5 BTC to Hal Finney"])
second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liss"])