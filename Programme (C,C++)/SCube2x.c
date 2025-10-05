#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Move definitions
int moveDefs[9][24] = {
    {2,0,3,1,20,21,6,7,4,5,10,11,12,13,14,15,8,9,18,19,16,17,22,23}, // U
    {1,3,0,2,8,9,6,7,16,17,10,11,12,13,14,15,20,21,18,19,4,5,22,23}, // U'
    {3,2,1,0,16,17,6,7,20,21,10,11,12,13,14,15,4,5,18,19,8,9,22,23}, // U2
    {0,9,2,11,6,4,7,5,8,13,10,15,12,22,14,20,16,17,18,19,3,21,1,23}, // R
    {0,22,2,20,5,7,4,6,8,1,10,3,12,9,14,11,16,17,18,19,15,21,13,23}, // R'
    {0,13,2,15,7,6,5,4,8,22,10,20,12,1,14,3,16,17,18,19,11,21,9,23}, // R2
    {0,1,19,17,2,5,3,7,10,8,11,9,6,4,14,15,16,12,18,13,20,21,22,23}, // F
    {0,1,4,6,13,5,12,7,9,11,8,10,17,19,14,15,16,3,18,2,20,21,22,23}, // F'
    {0,1,13,12,19,5,17,7,11,10,9,8,3,2,14,15,16,6,18,4,20,21,22,23}  // F2
};

char* move_names[9] = {"U", "U'", "U2", "R", "R'", "R2", "F", "F'", "F2"};

// Apply a move to the cube state
void do_move(int* state, int move, int* result) {
    for(int i = 0; i < 24; i++) {
        result[i] = state[moveDefs[move][i]];
    }
}

// Check if cube is solved
int is_solved(int* state) {
    for(int i = 0; i < 6; i++) {
        int base = state[4*i];
        for(int j = 1; j < 4; j++) {
            if(state[4*i + j] != base) {
                return 0;
            }
        }
    }
    return 1;
}

// Initialize solved state
void init_state(int* state) {
    for(int i = 0; i < 4; i++) state[i] = 0;     // White
    for(int i = 4; i < 8; i++) state[i] = 1;     // Red
    for(int i = 8; i < 12; i++) state[i] = 2;    // Green
    for(int i = 12; i < 16; i++) state[i] = 3;   // Yellow
    for(int i = 16; i < 20; i++) state[i] = 4;   // Orange
    for(int i = 20; i < 24; i++) state[i] = 5;   // Blue
}

// Simple IDA* search
char* ida_star_search(int* state, int depth, int* moves, int move_count, int last_move) {
    if(is_solved(state)) {
        // Build solution string
        char* solution = malloc(100);
        solution[0] = '\0';
        for(int i = 0; i < move_count; i++) {
            strcat(solution, move_names[moves[i]]);
            if(i < move_count - 1) strcat(solution, " ");
        }
        return solution;
    }

    if(depth == 0) return NULL;

    for(int move = 0; move < 9; move++) {
        // Don't do consecutive moves on same face
        if(move / 3 == last_move / 3) continue;

        int new_state[24];
        do_move(state, move, new_state);

        int new_moves[move_count + 1];
        for(int i = 0; i < move_count; i++) new_moves[i] = moves[i];
        new_moves[move_count] = move;

        char* solution = ida_star_search(new_state, depth - 1, new_moves, move_count + 1, move);
        if(solution != NULL) return solution;
    }

    return NULL;
}

// Main solve function
char* solve_cube(int* input_state) {
    int state[24];
    // Copy input state
    for(int i = 0; i < 24; i++) state[i] = input_state[i];

    // Try increasing depths
    for(int depth = 1; depth <= 12; depth++) {
        int moves[0];
        char* solution = ida_star_search(state, depth, moves, 0, -3);
        if(solution != NULL) return solution;
    }

    return "No solution found";
}

int main() {
    printf("Start With face: Up,Right,Front,Down,Left,Back 0=White,1=Red,2=Green,3=Yellow,4=Orange,5=Blue).\nEnter 24-digit cube state: ");
    char input[25];
    scanf("%24s", input);
    if(strlen(input) == 24) {
        int cube_state[24];
        for(int i = 0; i < 24; i++) {
            cube_state[i] = input[i] - '0';
        }
        char* solution = solve_cube(cube_state);
        // Save to file
        FILE* file = fopen("Solution.txt", "w");
        if(file != NULL) {
            fprintf(file, "Input: ");
            for(int i = 0; i < 24; i++) {
                fprintf(file, "%d", cube_state[i]);
                if(i < 23) fprintf(file, ",");
            }
            fprintf(file, "\nSolution: %s", solution);
            fclose(file);
        }
        printf("Solution: %s\n", solution);
        printf("Solution saved to Solution.txt\n");
        if(solution != NULL && strcmp(solution, "No solution found") != 0) {
            free(solution);
        }
    } else {
        printf("Error: Input must be exactly 24 digits\n");
    }

    return 0;
}
