class Solution
{
public:
    bool check(string palindrome)
    {
        string rev = palindrome;

        reverse(rev.begin(), rev.end());

        if (rev == palindrome)
            return true;

        return false;
    }

    string breakPalindrome(string palindrome)
    {

        if (palindrome.length() == 1)
            return "";

        for (int i = 0; i < palindrome.length(); i++)
        {
            if (palindrome[i] != 'a')
            {
                string checkS = palindrome;
                checkS[i] = 'a';
                if (check(checkS))
                    continue;
                else
                {
                    palindrome[i] = 'a';

                    return palindrome;
                }
            }
        }

        palindrome[palindrome.length() - 1] = 'b';
        return palindrome;
    }
};