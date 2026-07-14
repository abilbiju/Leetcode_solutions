class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Maps a character to its most recent index in the string
        char_index_map = {}
        max_length = 0
        left = 0  # Left boundary of our sliding window
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is in the map AND its last seen index 
            # falls inside our active window, we shrink the window.
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # Move 'left' past the previous duplicate occurrence
                left = char_index_map[current_char] + 1
                
            # Store or update the character's latest index position
            char_index_map[current_char] = right
            
            # Calculate current window size and maximize the result
            current_window_length = right - left + 1
            if current_window_length > max_length:
                max_length = current_window_length
                
        return max_length

        