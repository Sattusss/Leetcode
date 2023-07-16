from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Convert req_skills to a bit mask
        skill_to_bit = {}
        for i, skill in enumerate(req_skills):
            skill_to_bit[skill] = 1 << i

        # Convert people to a bit mask
        person_to_bit = []
        for person in people:
            bit = 0
            for skill in person:
                bit |= skill_to_bit[skill]
            person_to_bit.append(bit)

        # DP
        dp = {0: []}
        for i, bit in enumerate(person_to_bit):
            for prev_bit, prev_team in list(dp.items()):
                new_bit = prev_bit | bit
                if new_bit not in dp or len(dp[new_bit]) > len(prev_team) + 1:
                    dp[new_bit] = prev_team + [i]

        return dp[(1 << len(req_skills)) - 1]
    