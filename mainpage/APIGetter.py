from enkanetwork import EnkaNetworkAPI
from enkanetwork.model.stats import Stats
import asyncio


client = EnkaNetworkAPI(lang="en")  # Create an instance of the API client
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
    client = EnkaNetworkAPI(lang="en")

    def remove_zero_values(data_dict):
        """Removes key-value pairs with a value of 0 or "0%" from a dictionary.

        Args:
            data_dict: The dictionary to filter.

        Returns:
            A new dictionary with zero-value items removed.
        """

        return {key: value for key, value in data_dict.items() if value not in [0, "0%"]}

    async with client:
        data = await client.fetch_user(uid)

        character_stats = {}  # Dictionary to hold all characters' stats

        for character in data.characters:
            # Create a dictionary for this character's stats
            stat_dict = {}
            for stat in character.stats:
                stat_value = stat[1].to_rounded() if isinstance(stat[1], Stats) else stat[1].to_percentage_symbol()
                stat_dict[stat[0]] = stat_value

            # Remove zero values from this character's stats
            stat_dict = remove_zero_values(stat_dict)

            # Store this character's stats in the main dictionary
            character_stats[character.name] = stat_dict

        return character_stats  # Return the dictionary containing all characters' stats

