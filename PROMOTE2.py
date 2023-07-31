from telethon import TelegramClient, events
import asyncio

api_id = 28608773 # ganti dengan api_id Anda
api_hash = '3d63f46adc9dece0665bbb4fb5534c61' 

async def send_message(client, username, message, timer):
    session = 1
    while session <= 1000:  # Jumlah sesi yang diinginkan
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
    async with TelegramClient('bot3', api_id, api_hash) as client:
        target_usernames = ['LPM_BBG_MMK_DDK_BBB', 'lpm_ddk_bbg_rprl','LPM_DDK_BBG_BBB_MMK', 'lpm_bbg_ddk', 'LPM_DDK_BBG_MMK', 'LPMBBGDDKIDGAR', 'lpm_ddk_bbb_bbg']
        message = '''
        CC BARU NETES, NO KACANG SOKAPIN
        FREE OS, PAP, RPRL

https://t.me/+aYGP-EKcTdFkMDg1
        
https://t.me/+aYGP-EKcTdFkMDg1
https://t.me/+aYGP-EKcTdFkMDg1'''
       

        timers = [30, 30, 30, 30, 30, 30]  # Timer untuk setiap pengguna (dalam detik)

        tasks = []
        for username, timer in zip(target_usernames, timers):
            task = send_message(client, username, message, timer)
            tasks.append(task)

        await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
