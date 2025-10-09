#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LEN 1000

int main() {
    char text[MAX_LEN];
    printf("Example: 'unKNOwyyyOU' → Result Is: 'KNO'\n");

    while (1) {
        printf("\nEnter a string (or 'q' to quit): ");
        if (!fgets(text, sizeof(text), stdin)) break;

        // Remove trailing newline if any
        text[strcspn(text, "\n")] = 0;

        if (strcmp(text, "q") == 0 || strcmp(text, "Q") == 0) break;

        int len = strlen(text);
        if (len < 5) {
            printf("Result Is: Input too short (min 5 characters)\n");
            continue;
        }

        // Check if all characters are alphanumeric
        int valid = 1;
        for (int i = 0; i < len; i++) {
            if (!isalnum((unsigned char)text[i])) {
                valid = 0;
                break;
            }
        }
        if (!valid) {
            printf("Error: Enter 'alpha-numeric' characters only!\n");
            continue;
        }

        int max_start = 0, max_len = 0;
        int curr_start = -1, curr_len = 0;

        for (int i = 0; i < len; i++) {
            if (isupper((unsigned char)text[i])) {
                if (curr_start == -1) curr_start = i;
                curr_len++;
            } else {
                if (curr_len > max_len) {
                    max_len = curr_len;
                    max_start = curr_start;
                }
                curr_start = -1;
                curr_len = 0;
            }
        }
        // Check last sequence
        if (curr_len > max_len) {
            max_len = curr_len;
            max_start = curr_start;
        }

        if (max_len > 0) {
            printf("Result Is: ");
            for (int i = max_start; i < max_start + max_len; i++) {
                putchar(text[i]);
            }
            printf("\n");
        } else {
            printf("The result is (find_max_capital sequence upper): No uppercase sequence found.\n");
        }
    }

    return 0;
}
