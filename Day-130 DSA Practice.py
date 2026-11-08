(* 744. Find Smallest Letter Greater Than Target *)
(* You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.*)
class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[left % len(letters)]

(* 1024. Video Stitching *)
(* You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths. *)
class Solution:
    def videoStitching(self, clips, time):
        clips.sort()
        count = 0
        current_end = 0
        farthest = 0
        i = 0
        while current_end < time:
            while i < len(clips) and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == current_end:
                return -1
            count += 1
            current_end = farthest
        return count
