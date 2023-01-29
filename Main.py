import requests
import json
import time

while True:


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

  content = "Last 24h reward number: 0.0{} XMR\nLast 24h reward number in EUR: {:.2f}\nActual Round Share: {}%\nNumber of workers online: {}\nLast Block XMR reward: 0.000{}\nTotal payout :{}\nCurrent Hashrate : {} KH/s\nAverage Hashrate : {} KH/s\nNetwork Difficulty: {} G".format(last_reward_num, eur, last_reward_percentage, workerOnline, Last_Block_XMR_reward, paymentsTotal, currentHashrate, Hashrate, difficulty)

  def send_to_discord(content):
      webhook_url = "https://discord.com/api/webhooks/1069319353956323348/hbY_Ouh7lwSymAf9Lk6yE4e2tP-Fuaaq-axphwlgVgDxEsQxMdvdI5KqCpwuJfm0bDFF"
      payload = {
          "avatar_url": "https://cdn.iconscout.com/icon/free/png-256/monero-3629611-3032309.png",
          "username": "2miners XMR pool",
          "embeds": [
              {
                  "title": "2miners XMR Pool Statistics",
                  "description": content,
                  "color": 14177041,
                  "footer": {
                      "text": "By Skippyturtle#4893"
                  }
              }
          ]
      }


      headers = {"Content-Type": "application/json"}
      try:
          response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
          response.raise_for_status()
          print("Payload sent to Discord successfully")
      except requests.exceptions.RequestException as error:
          print(f"Failed to send payload to Discord: {error}")

  send_to_discord(content)
  print(content)
  time.sleep(3600)
