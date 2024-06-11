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
            # Calculate damage if stats are present and numeric
            damage_values = {
                "Normal": stats["FIGHT_PROP_CUR_ATTACK"] * (scaling * 0.01),
                "NormalCrit": (stats["FIGHT_PROP_CUR_ATTACK"] * (scaling * 0.01)) * (
                        stats["FIGHT_PROP_CRITICAL_HURT"] * 0.01
                ),
                "AvgCrit": stats["FIGHT_PROP_CUR_ATTACK"]
                                     * (stats["FIGHT_PROP_CRITICAL"] * 0.01)
                                     * (1 + (stats["FIGHT_PROP_CRITICAL_HURT"] * 0.01))
                                     + stats["FIGHT_PROP_CUR_ATTACK"]
                                     * (1 - stats["FIGHT_PROP_CRITICAL"] * 0.01),
            }

        damage_dict[character_name] = damage_values

    return damage_dict