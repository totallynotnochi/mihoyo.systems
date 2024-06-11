def calculate_damage(character_stats, scaling):

    damage_dict = {}
    required_keys = ["FIGHT_PROP_CUR_ATTACK", "FIGHT_PROP_CRITICAL_HURT", "FIGHT_PROP_CRITICAL"]

    for character_name, stats in character_stats.items():
        # Check for missing or non-numeric stats
        if not all(
                key in stats and isinstance(stats[key], (int, float)) for key in required_keys
        ):
            damage_values = {dmg_type: "N/A" for dmg_type in ["Normal", "Normal Crit", "Normal Crit (AVG)"]}
        else:

            normal = stats["FIGHT_PROP_CUR_ATTACK"] * (scaling * 0.01)
            normal_crit_dmg = ((stats["FIGHT_PROP_CUR_ATTACK"] * (scaling * 0.01)) * (stats["FIGHT_PROP_CRITICAL_HURT"] * 0.01))
            crit_rate = stats["FIGHT_PROP_CRITICAL"] * 0.01

            # Calculate damage if stats are present and numeric
            damage_values = {
                "Normal": normal,
                "NormalCrit": normal + normal_crit_dmg,
                "AvgCrit": normal + (normal_crit_dmg * crit_rate)
            }

        damage_dict[character_name] = damage_values

    return damage_dict