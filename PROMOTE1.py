from telethon import TelegramClient, events
import asyncio

api_id = 23704889 # ganti dengan api_id Anda
api_hash = 'bf05c4fe9eb2a124a5843af54a1dd5e1' 

async def send_message(client, username, message, timer):
    session = 1
    while session <= 2000:  # Jumlah sesi yang diinginkan
        print(f'Sesi ke-{session} untuk pengguna {username}')
        try:
            await client.send_message(username, message)
            print(f'Pesan terkirim ke pengguna {username}')
        except Exception as e:
            if 'FloodWaitError' in str(e):
                wait_time = int(str(e).split('for ')[1].split(' seconds')[0])
                print(f'Tunggu {wait_time} detik sebelum mencoba lagi untuk pengguna {username}')
                await asyncio.sleep(wait_time)
                continue
            else: 
                print(f'Kesalahan saat mengirim pesan ke pengguna {username}: {e}')
        await asyncio.sleep(timer)
        session += 1

async def main():
    async with TelegramClient('bot2', api_id, api_hash) as client:
        target_usernames = ['https://t.me/lpm_cari_cp_suami_rprl','https://t.me/lpm_cari_cp_suami_rprl','https://t.me/lpm_cari_fambest','https://t.me/LPM_Roleplayer','https://t.me/lpm_cari_cp_rprl','https://t.me/LPM_Roleplayers','https://t.me/lpm_roleplay']
        message = '''----------------------------
CC RPRL, FREE OS
SOKAPIN

NO KACANG
NOBAR/DEMUS

https://t.me/+aYGP-EKcTdFkMDg1
https://t.me/+aYGP-EKcTdFkMDg1
'''       

        timers = [30, 30, 30, 30, 33, 30, 30, 50, 50, 60, 40, 40, 35, 30]  # Timer untuk setiap pengguna (dalam detik)

        tasks = []
        for username, timer in zip(target_usernames, timers):
            task = send_message(client, username, message, timer)
            tasks.append(task)

        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
