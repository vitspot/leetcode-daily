class Solution
{
public:
    int numUniqueEmails(vector<string> &emails)
    {
        set<string> s;

        for (int i = 0; i < emails.size(); i++)
        {
            string e = "";
            int ignore = false;
            int domain = false;

            for (int j = 0; j < emails[i].length(); j++)
            {
                if (emails[i][j] == '.' && domain == false)
                    continue;

                if (emails[i][j] == '+' && domain == false)
                {
                    ignore = true;
                    continue;
                }

                if (emails[i][j] == '@')
                {
                    domain = true;
                }

                if (domain)
                {
                    e += emails[i][j];
                    continue;
                }

                if (ignore == false)
                {
                    e += emails[i][j];
                }
            }

            s.insert(e);
        }

        return s.size();
    }
};