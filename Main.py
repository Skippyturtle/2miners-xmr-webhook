import requests
import json

url_rewards = "https://xmr.2miners.com/api/accounts/45Jq4Gokx5BbwLnrLRUFquG4uSZ4mkcHDMYjibNBgrD291wG4Pz8bcx9KScWycUjW9iiejGY5PoQ9eMUsZaZ7Z6S1XggBKi"
response_rewards = requests.get(url_rewards)
data_rewards = response_rewards.json()

last_reward = data_rewards["24hreward"]
last_reward_num = data_rewards["24hnumreward"]
workerOnline = int(data_rewards["minerCharts"][-1]["workerOnline"])
rewards = data_rewards["rewards"]
last_reward = rewards[0]["reward"]
last_reward_percentage = rewards[0]["percent"]
Last_Block_XMR_reward = data_rewards["sumrewards"][0]["reward"]
paymentsTotal = data_rewards["paymentsTotal"]
Hashrate = int(data_rewards["minerCharts"][-1]["minerHash"])
currentHashrate = data_rewards["currentHashrate"]

url_difficulty = "https://xmr.2miners.com/api/stats"
response_difficulty = requests.get(url_difficulty)
data_difficulty = response_difficulty.json()
difficulty = data_difficulty["nodes"][0]["difficulty"]

def xmr_to_eur(xmr):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=eur"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["monero"]["eur"]
    return xmr * exchange_rate

eur = xmr_to_eur(last_reward_num)

print("Last 24h reward number: 0.0{} XMR".format(last_reward_num))
print("Last 24h reward number in EUR: {:.2f}".format(eur))
print("Actual Round Share: {}%".format(last_reward_percentage))
print("Number of workers online: {}".format(workerOnline))
print("Last Block XMR reward: 0.000{}".format(Last_Block_XMR_reward))
print("Total payout :{}".format(paymentsTotal))
print("Current Hashrate : {} KH/s".format(currentHashrate))
print("Average Hashrate : {} KH/s".format(Hashrate))
print("Network Difficulty: {} G".format(difficulty))
