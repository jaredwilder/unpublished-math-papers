#include <algorithm>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

using namespace std;
__extension__ typedef unsigned __int128 U128;

static constexpr int N = 72;
static vector<U128> compatibility;
static vector<vector<U128>> third_vertex_forbidden;
static int best = 0;
static long long search_nodes = 0;
static set<U128> extremizers;

static int popcount(U128 value) {
    return __builtin_popcountll(static_cast<uint64_t>(value))
        + __builtin_popcountll(static_cast<uint64_t>(value >> 64));
}

static int lowbit_index(U128 value) {
    const uint64_t low = static_cast<uint64_t>(value);
    if (low != 0) return __builtin_ctzll(low);
    return 64 + __builtin_ctzll(static_cast<uint64_t>(value >> 64));
}

static vector<int> members(U128 mask) {
    vector<int> result;
    while (mask != 0) {
        const int vertex = lowbit_index(mask);
        result.push_back(vertex);
        mask &= ~(U128(1) << vertex);
    }
    return result;
}

static void color_sort(U128 candidates, vector<int>& vertices, vector<int>& bounds) {
    int color = 0;
    U128 remaining = candidates;
    while (remaining != 0) {
        ++color;
        U128 available = remaining;
        while (available != 0) {
            const int vertex = lowbit_index(available);
            const U128 bit = U128(1) << vertex;
            vertices.push_back(vertex);
            bounds.push_back(color);
            remaining &= ~bit;
            available &= ~bit;
            available &= ~compatibility[vertex];
        }
    }
}

static void expand(U128 chosen, U128 candidates) {
    ++search_nodes;
    if (candidates == 0) {
        const int size = popcount(chosen);
        if (size > best) { best = size; extremizers.clear(); extremizers.insert(chosen); }
        else if (size == best) extremizers.insert(chosen);
        return;
    }

    vector<int> vertices;
    vector<int> bounds;
    color_sort(candidates, vertices, bounds);
    for (int index = static_cast<int>(vertices.size()) - 1; index >= 0; --index) {
        if (popcount(chosen) + bounds[index] < best) return;
        const int vertex = vertices[index];
        const U128 bit = U128(1) << vertex;
        if ((candidates & bit) == 0) continue;
        U128 forbidden = 0;
        U128 selected = chosen;
        while (selected != 0) {
            const int other = lowbit_index(selected);
            selected &= ~(U128(1) << other);
            forbidden |= third_vertex_forbidden[vertex][other];
        }
        expand(chosen | bit, candidates & compatibility[vertex] & ~forbidden);
        candidates &= ~bit;
    }

    const int size = popcount(chosen);
    if (size > best) { best = size; extremizers.clear(); extremizers.insert(chosen); }
    else if (size == best) extremizers.insert(chosen);
}

int main() {
    constexpr int modulus = 73;
    set<U128> forbidden_edges;

    for (int x = 1; x < modulus; ++x) {
        for (int y = 1; y < modulus; ++y) {
            int z = (x + y) % modulus;
            if (z != 0) {
                forbidden_edges.insert((U128(1) << (x - 1)) | (U128(1) << (y - 1)) | (U128(1) << (z - 1)));
            }
            z = static_cast<int>(static_cast<long long>(x) * y % modulus);
            if (z != 0) {
                forbidden_edges.insert((U128(1) << (x - 1)) | (U128(1) << (y - 1)) | (U128(1) << (z - 1)));
            }
        }
    }

    for (int first = 1; first < modulus; ++first) {
        for (int middle = 1; middle < modulus; ++middle) {
            int last = (2 * middle - first) % modulus;
            if (last < 0) last += modulus;
            if (last != 0 && first != middle && first != last && middle != last) {
                forbidden_edges.insert((U128(1) << (first - 1)) | (U128(1) << (middle - 1)) | (U128(1) << (last - 1)));
            }
        }
    }

    const U128 full = (U128(1) << N) - 1;
    U128 forced = 0;
    compatibility.assign(N, 0);
    third_vertex_forbidden.assign(N, vector<U128>(N));
    for (int vertex = 0; vertex < N; ++vertex) compatibility[vertex] = full ^ (U128(1) << vertex);

    for (U128 edge : forbidden_edges) {
        const auto vertices = members(edge);
        if (vertices.size() == 1) {
            forced |= U128(1) << vertices[0];
        } else if (vertices.size() == 2) {
            compatibility[vertices[0]] &= ~(U128(1) << vertices[1]);
            compatibility[vertices[1]] &= ~(U128(1) << vertices[0]);
        } else if (vertices.size() == 3) {
            const int a = vertices[0], b = vertices[1], c = vertices[2];
            third_vertex_forbidden[a][b] |= U128(1) << c;
            third_vertex_forbidden[b][a] |= U128(1) << c;
            third_vertex_forbidden[a][c] |= U128(1) << b;
            third_vertex_forbidden[c][a] |= U128(1) << b;
            third_vertex_forbidden[b][c] |= U128(1) << a;
            third_vertex_forbidden[c][b] |= U128(1) << a;
        } else return 3;
    }

    for (int vertex = 0; vertex < N; ++vertex) compatibility[vertex] &= ~forced;
    expand(0, full & ~forced);

    cout << "modulus=73\n"
         << "edge_count=" << forbidden_edges.size() << "\n"
         << "maximum=" << best << "\n"
         << "extremal_count=" << extremizers.size() << "\n"
         << "search_nodes=" << search_nodes << "\n";

    int index = 0;
    for (U128 extremizer : extremizers) {
        cout << "extremizer_" << index++ << "=";
        const auto vertices = members(extremizer);
        for (size_t i = 0; i < vertices.size(); ++i) {
            if (i != 0) cout << ",";
            cout << vertices[i] + 1;
        }
        cout << "\n";
    }

    return (best == 12 && extremizers.size() == 3 && forbidden_edges.size() == 7422) ? 0 : 4;
}