/*
# 7. Create a C program that accepts an IPv4 address and subnet mask in dotted decimal format, and outputs:
# a. Network ID
# b. Broadcast Address
# c. First and Last Host Address
# d. CIDR notation
# e. Number of valid hosts
# f. IP Address Class (A/B/C/D/E).

 * subnet_calc.c
 * Accepts an IPv4 address and subnet mask (dotted decimal) and prints:
 *   Network ID, Broadcast Address, First/Last Host, CIDR, Usable Hosts, Class.
 *
 * Compile: gcc -Wall -Wextra -o subnet_calc subnet_calc.c
 * Run:     ./subnet_calc
 */

 
#include <stdio.h>
#include <stdint.h>
 
static void show(const char *label, uint32_t x)
{
    printf("%-18s: %u.%u.%u.%u\n", label, x >> 24, (x >> 16) & 255, (x >> 8) & 255, x & 255);
}
 
int main(void)
{
    unsigned a, b, c, d, m, n, o, p;
 
    printf("IP address : ");  scanf("%u.%u.%u.%u", &a, &b, &c, &d);
    printf("Subnet mask: ");  scanf("%u.%u.%u.%u", &m, &n, &o, &p);
 
    uint32_t ip   = a << 24 | b << 16 | c << 8 | d;
    uint32_t mask = m << 24 | n << 16 | o << 8 | p;
    uint32_t net  = ip & mask, bc = net | ~mask;
    int cidr = __builtin_popcount(mask);                 /* count the 1 bits */
    unsigned long long hosts = cidr >= 31 ? 33ULL - cidr : (1ULL << (32 - cidr)) - 2;
 
    show("Network ID", net);
    show("Broadcast Address", bc);
    show("First Host", cidr < 31 ? net + 1 : net);
    show("Last Host",  cidr < 31 ? bc - 1  : bc);
    printf("%-18s: /%d\n", "CIDR Notation", cidr);
    printf("%-18s: %llu\n", "Valid Hosts", hosts);
    printf("%-18s: %c\n", "IP Class", a < 128 ? 'A' : a < 192 ? 'B' : a < 224 ? 'C' : a < 240 ? 'D' : 'E');
    return 0;
}
 

// #include <stdio.h>
// #include <stdint.h>
// #include <string.h>
// #include <ctype.h>

// /* Parse dotted-decimal into a 32-bit value. Returns 1 on success, 0 on failure. */
// static int parse_ipv4(const char *s, uint32_t *out)
// {
//     unsigned a, b, c, d;
//     char extra = '\0';

//     if (s == NULL || *s == '\0')
//         return 0;

//     /* Reject anything that is not a digit or a dot (blocks "-1", spaces, etc.) */
//     for (const char *p = s; *p; p++)
//         if (!isdigit((unsigned char)*p) && *p != '.')
//             return 0;

//     if (sscanf(s, "%u.%u.%u.%u%c", &a, &b, &c, &d, &extra) != 4)
//         return 0;
//     if (a > 255 || b > 255 || c > 255 || d > 255)
//         return 0;

//     *out = (a << 24) | (b << 16) | (c << 8) | d;
//     return 1;
// }

// static void print_ip(const char *label, uint32_t ip)
// {
//     printf("%-18s: %u.%u.%u.%u\n", label,
//            (ip >> 24) & 0xFF, (ip >> 16) & 0xFF, (ip >> 8) & 0xFF, ip & 0xFF);
// }

// /* A valid mask is contiguous 1s followed by contiguous 0s. */
// static int is_valid_mask(uint32_t mask)
// {
//     uint32_t inv = ~mask;
//     return (inv & (inv + 1)) == 0;
// }

// static int cidr_from_mask(uint32_t mask)
// {
//     int n = 0;
//     while (mask & 0x80000000u) {
//         n++;
//         mask <<= 1;
//     }
//     return n;
// }

// static char ip_class(uint32_t ip)
// {
//     unsigned first = (ip >> 24) & 0xFF;
//     if (first < 128) return 'A';
//     if (first < 192) return 'B';
//     if (first < 224) return 'C';
//     if (first < 240) return 'D';
//     return 'E';
// }

// static void read_line(const char *prompt, char *buf, size_t size)
// {
//     printf("%s", prompt);
//     if (!fgets(buf, (int)size, stdin)) {
//         buf[0] = '\0';
//         return;
//     }
//     buf[strcspn(buf, "\r\n")] = '\0';
// }

// int main(void)
// {
//     char ip_str[64], mask_str[64];
//     uint32_t ip, mask;

//     read_line("Enter IPv4 address (e.g. 192.168.10.37): ", ip_str, sizeof ip_str);
//     read_line("Enter subnet mask  (e.g. 255.255.255.0): ", mask_str, sizeof mask_str);

//     if (!parse_ipv4(ip_str, &ip)) {
//         fprintf(stderr, "Error: invalid IPv4 address.\n");
//         return 1;
//     }
//     if (!parse_ipv4(mask_str, &mask)) {
//         fprintf(stderr, "Error: invalid subnet mask format.\n");
//         return 1;
//     }
//     if (!is_valid_mask(mask)) {
//         fprintf(stderr, "Error: subnet mask is not contiguous.\n");
//         return 1;
//     }

//     uint32_t network   = ip & mask;
//     uint32_t broadcast = network | ~mask;
//     int      prefix    = cidr_from_mask(mask);
//     uint32_t first, last;
//     uint64_t hosts;

//     if (prefix == 32) {            /* single host route */
//         first = last = ip;
//         hosts = 1;
//     } else if (prefix == 31) {     /* point-to-point link, RFC 3021 */
//         first = network;
//         last  = broadcast;
//         hosts = 2;
//     } else {
//         first = network + 1;
//         last  = broadcast - 1;
//         hosts = (1ULL << (32 - prefix)) - 2;
//     }

//     printf("\n===== Subnet Details =====\n");
//     print_ip("Network ID", network);
//     print_ip("Broadcast Address", broadcast);
//     print_ip("First Host", first);
//     print_ip("Last Host", last);
//     printf("%-18s: %u.%u.%u.%u/%d\n", "CIDR Notation",
//            (network >> 24) & 0xFF, (network >> 16) & 0xFF,
//            (network >> 8) & 0xFF, network & 0xFF, prefix);
//     printf("%-18s: %llu\n", "Valid Hosts", (unsigned long long)hosts);
//     printf("%-18s: %c\n", "IP Class", ip_class(ip));

//     return 0;
// }
