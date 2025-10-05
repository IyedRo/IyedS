#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void generate_words(char *tokens, int length, int length_max)
{
    int length_tokens = strlen(tokens);
    long long number_words = (long long)pow(length_tokens, length);
    char word[length + 1];

    FILE *file = fopen("lexgen.txt", "w");
    if (!file)
    {
        printf("Error opening file!\n");
        return;
    }

    if (length_max == -1)
    {
        for (long long num = 0; num < number_words; num++)
        {
            int temp = num;
            for (int i = 0; i < length; i++)
            {
                word[length - i - 1] = tokens[temp % length_tokens];
                temp /= length_tokens;
            }
            word[length] = '\0';
            fprintf(file, "%s\n", word);
        }
    }
    else
    {
        for (int current_length = length; current_length <= length_max; current_length++)
        {
            long long number_words_ones = (long long)pow(length_tokens, current_length);
            for (long long num = 0; num < number_words_ones; num++)
            {
                int temp = num;
                for (int i = 0; i < current_length; i++)
                {
                    word[current_length - i - 1] = tokens[temp % length_tokens];
                    temp /= length_tokens;
                }
                word[current_length] = '\0';
                fprintf(file, "%s\n", word);
            }
        }
    }
    fclose(file);
    printf("Finished: words generated. Output written to 'lexgen.txt'.\n");
}

char* combine_token_categories(char *response_user, char **token_categories)
{
    static char combined[1024];
    int index = 0;
    for (int i = 0; i < strlen(response_user); i++)
    {
        int token_index = response_user[i] - '1';
        strcat(combined, token_categories[token_index]);
    }
    return combined;
}

void word_length_input(char *tokens)
{
    int mode;
    printf("Choose length mode - fixed (1) or range (2): ");
    scanf("%d", &mode);
    if (mode == 1)
    {
        int length;
        while (1)
        {
            printf("Enter fixed word length (1-63): ");
            scanf("%d", &length);
            if (length >= 1 && length <= 63)
            {
                printf("\ntokens= %s\nlength= %d\n", tokens, length);
                generate_words(tokens, length, -1);  // -1 indicates fixed length
                break;
            }
            printf("Invalid input. Please enter a number between 1 and 63.\n");
        }
    }
    else
    {
        int length, length_max;
        while (1)
        {
            printf("Enter minimum word length (1-63): ");
            scanf("%d", &length);
            printf("Enter maximum word length (1-63): ");
            scanf("%d", &length_max);
            if (length >= 1 && length <= 63 && length_max >= 1 && length_max <= 63 && length <= length_max)
            {
                printf("\ntokens= %s\nlength_minimum= %d\nlength_maximum= %d\n", tokens, length, length_max);
                generate_words(tokens, length, length_max);
                break;
            }
            printf("Invalid input. Please enter valid lengths between 1 and 63.\n");
        }
    }
}

void lexical_generator()
{
    printf("LG] Lexical Generator\n");
    char *token_categories[] =
    {
        "0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    };
    char *token_labels[] =
    {
        "Digits", "Lowercase Letters", "Uppercase Letters"
    };
    printf("0) Custom\n");
    for (int i = 0; i < 3; i++)
    {
        printf("%d) %s: %s\n", i + 1, token_labels[i], token_categories[i]);
    }

    char response_user[4];
    while (1)
    {
        printf("Enter your token response_user: ");
        scanf("%s", response_user);
        if (strlen(response_user) >= 1 && strlen(response_user) <= 3)
        {
            int valid = 1;
            for (int i = 0; i < strlen(response_user); i++)
            {
                if (response_user[i] < '0' || response_user[i] > '3')
                {
                    valid = 0;
                    break;
                }
            }
            if (valid) break;
        }
        printf("Invalid input. Choose 1 to 3 characters from [0-3].\n");
    }

    if (strchr(response_user, '0'))
    {
        if (strlen(response_user) == 1)
        {
            char custom_tokens[256];
            printf("Enter your custom token set: ");
            scanf("%s", custom_tokens);
            word_length_input(custom_tokens);
        }
        else
        {
            printf("Custom option must be used alone.\n");
        }
    }
    else
    {
        char *tokens = combine_token_categories(response_user, token_categories);
        printf("Using token set: %s\n", tokens);
        word_length_input(tokens);
    }
}

int main()
{
    char repeat = ' ';
    while (repeat != 'q' && repeat != 'Q')
    {
        lexical_generator();
        printf("Press any key to repeat, or 'q' to quit: ");
        getchar();
        repeat = getchar();
    }
    printf("\nIYR] أهلاً وسهلاً بك! أتمنى أن تجد كل ما تحتاجه وتستفيد منه. السلام عليكم ورحمة الله وبركاته! 😊\nExit!!!\n");
    return 0;
}
