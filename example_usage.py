from client import MultiAgentConsensusVotingProtocolClient

def main():
    client = MultiAgentConsensusVotingProtocolClient()
    res = client.deliberate_proposal()
    print('Multi-Agent Consensus: ' + res['deliberation_id'] + ' (' + res['outcome'] + ')')
    print('Approval Ratio: ' + str(res['approval_ratio']) + ' | Margin: ' + str(res['bft_safety_margin']))
    print('Dossier URL: ' + res['dossier_url'])

if __name__ == '__main__':
    main()
