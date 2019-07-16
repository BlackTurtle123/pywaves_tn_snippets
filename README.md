# pywaves_tn_snippets

Snippets for TurtleNetwork with pywaves

Chars:
- 
- mainnet: 'L' 
- testnet: 'l'

Fees:
-
- Transfer: 0.02TN
- Create-alias: 10TN
- Exchange 0.04TN
- Issue Token: 1000TN
- Reissue: 1000TN
- Burn 0.02TN
- Lease 0.02TN
- Lease cancel: 0.02TN
- Set-asset- script: 1TN
- Set-account- script: 1TN
- Mass-transfer: 0.03 TN + 0.01TN for each recipient
    - Sponsor-asset-fee: 10TN
- Data: 0.021 TN minimal fee


Scripts:
-
- [Script to lock an account till a certain height](lock_till_height.py)
- [Script to send a tx to an address at every block](send_each_block.py)
