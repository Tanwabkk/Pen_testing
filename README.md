# Pen-Testing & Cybersecurity Lab

A collection of educational cybersecurity scripts, vulnerability demonstrations, and proof-of-concept code samples for learning secure coding practices, penetration testing techniques, and application defense.

## Purpose
The goal of this repository is to serve as a personal sandbox and reference guide for understanding how common software vulnerabilities occur, how they can be tested locally, and how to properly secure code against them. As well as anything you do related to IP address use your own device or you virtual machine as hacking or scanning other network that is not yours could give you trouble. 

## Topics Covered
* **Injection Flaws:** Understanding SQL injection (SQLi), command injection, and input sanitization failures through vulnerable versus secure code implementations.
* **Authentication & Access Control:** Examining session management flaws, password handling, and privilege escalation vectors.
* **Web Security:** Exploring common web vulnerabilities (XSS, CSRF, insecure endpoints) using lightweight, dependency-free local environments.
* **Defensive Engineering:** Implementing robust mitigation strategies like parameterized queries, input validation, and least-privilege configurations.

## Recommended Hardware & OS Setup
For a system optimized for cybersecurity, penetration testing, and virtualized lab environments, prioritize an AMD Ryzen 7 (7000/8000 series) or Intel Core i7 (13th/14th Gen) processor featuring at least 8 cores, 16 threads, and dedicated hardware virtualization support (VT-x/AMD-V) to run multiple operating systems concurrently. Pair this with 32 GB of DDR5 RAM to handle resource-heavy tools like Burp Suite and Wireshark alongside simultaneous virtual machines, and a fast 1 TB NVMe PCIe 4.0 SSD for high-speed read/write performance when loading large disk images, memory dumps, and snapshot states. For GPU-accelerated hash cracking with Hashcat or John the Ripper, an NVIDIA GeForce RTX 4060 (8GB VRAM) provides excellent CUDA-supported performance. On the networking side, ensure the system features Wi-Fi 6E/7 for broad wireless compatibility, a physical Gigabit RJ-45 Ethernet port (or a high-speed USB-C adapter) for direct packet sniffing and network auditing, and multiple USB 3.2 Type-A ports to host external wireless pentesting adapters like Alfa chipsets. If choosing a laptop form factor, aim for a 15.6" or 16" anti-glare IPS display, an 80Wh+ battery, and a host OS like Windows 11 Pro or Linux running VMware Workstation, VirtualBox, or KVM.

## Getting Started
Most scripts in this repository are written in Python using standard libraries to minimize setup friction. Clone the repository and navigate to the specific directory of the script or experiment you wish to run:

```bash
git clone [https://github.com/Tanwabkk/pen-testing.git](https://github.com/Tanwabkk/pen-testing.git)
cd pen-testing
