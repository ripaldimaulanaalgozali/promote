from telethon import TelegramClient, events
import asyncio

api_id = 28608773 # ganti dengan api_id Anda
api_hash = '3d63f46adc9dece0665bbb4fb5534c61' 

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
    async with TelegramClient('bot1', api_id, api_hash) as client:
        target_usernames = ['https://t.me/lpm_roleplayer_1','https://t.me/lpm_roleplayer_23',
'https://t.me/LPM_Roleplayer_2','https://t.me/lpm_cari_cp_pacar','https://t.me/lpm_cari_cp_fambest_rp','https://t.me/lpm_cari_cp_temen_rprl','https://t.me/lpm_rp_cari_cp']
        message = '''SOKAPIN, FREE OS, RP/RPRL ‼️
NO KACANG SOKAPIN

https://t.me/+aYGP-EKcTdFkMDg1
https://t.me/+aYGP-EKcTdFkMDg1
https://t.me/+aYGP-EKcTdFkMDg1   '''
       

        timers = [30, 30, 30, 30, 30, 30, 35, 50, 50, 60, 40, 40, 35, 30]  # Timer untuk setiap pengguna (dalam detik)

        tasks = []
        for username, timer in zip(target_usernames, timers):
            task = send_message(client, username, message, timer)
            tasks.append(task)

        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
