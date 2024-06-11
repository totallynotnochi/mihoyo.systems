from enkanetwork import EnkaNetworkAPI
from enkanetwork.model.stats import Stats
import asyncio

client = EnkaNetworkAPI(lang="en")
genshin_data = {}


async def api_getter(uid):
    async with client:
        try:
            data = await client.fetch_user(uid)

            genshin_data['uid'] = data.uid
            genshin_data['playerInfo'] = data.player
            genshin_data['avatarInfoList'] = data.characters
            genshin_data["ttl"] = data.ttl

            if hasattr(data.player, 'stats'):
                genshin_data['stats'] = data.player.stats
            else:
                genshin_data['stats'] = None

            return genshin_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None


async def CharacterStats(uid):
    def remove_zero_values(data_dict):
        """Removes key-value pairs with a value of 0 or "0%" from a dictionary."""
        return {k: v for k, v in data_dict.items() if v not in [0, "0%"]}

    async with client:
        data = await client.fetch_user(uid)

        character_stats = {}
        for character in data.characters:
            stat_dict = {
                stat[0]: (
                    stat[1].to_rounded()
                    if isinstance(stat[1], Stats)
                    else stat[1].to_percentage_symbol()
                )
                for stat in character.stats
            }

            stat_dict = remove_zero_values(stat_dict)  # Filter out zero values
            stat_dict = {
                k: float(v.strip('%')) if isinstance(v, str) and '%' in v else v
                for k, v in stat_dict.items()
            }
            character_stats[character.name] = stat_dict

        return character_stats



