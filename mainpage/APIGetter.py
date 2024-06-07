from enkanetwork import EnkaNetworkAPI
import asyncio

client = EnkaNetworkAPI()  # Create an instance of the API client
genshin_data = {}


async def api_getter(uid):
    async with client:
        try:
            data = await client.fetch_user(uid)

            genshin_data['uid'] = data.uid
            genshin_data['playerInfo'] = data.player
            genshin_data['avatarInfoList'] = data.characters

            # Check if 'stats' exists before accessing it
            if hasattr(data.player, 'stats'):
                genshin_data['stats'] = data.player.stats
            else:
                # Handle the case where stats are not available
                genshin_data['stats'] = None  # or some default value

            return genshin_data

        except Exception as e:
            print(f"Error fetching data: {e}")
            return None