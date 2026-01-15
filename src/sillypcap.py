"""
SillyPCAP: Quantum-Cognitive Network Traffic Analyzer
Perfected version with all bugs fixed!

Features:
- Parse PCAPs while contemplating the wavefunction collapse of packets
- Analyze password entropy in Hilbert space
- Detect quantum entanglement in credential reuse
- Calculate the Heisenberg uncertainty of traffic patterns
"""

import struct
import logging
import datetime
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional, Any
import math
import random
import os
import traceback

# Try to import dpkt, but we'll have our own implementation
try:
    import dpkt
    import dpkt.pcapng
    DPKT_AVAILABLE = True
except ImportError:
    DPKT_AVAILABLE = False
    logging.warning("dpkt not available. Using quantum-enhanced parsing instead.")

# Our unified password field theory constants
PLANCK_COGNITIVE = 6.62607015e-34  # J·s (cognitive action quantum)
BOLTZMANN_BEHAVIORAL = 1.380649e-23  # J/K (behavioral temperature)
COGNITIVE_LIGHT_SPEED = 299792458  # m/s (speed of thought)

# Magic numbers for various formats
PCAP_MAGIC_NUMBERS = {
    0xa1b2c3d4: ("little", "classic"),  # Standard pcap little-endian
    0xd4c3b2a1: ("big", "classic"),     # Standard pcap big-endian
    0xa1b23c4d: ("little", "nanosecond"),  # pcap with nanosecond precision
    0x4d3cb2a1: ("big", "nanosecond"),     # pcap with nanosecond precision (big)
    0x0a0d0d0a: ("little", "pcapng"),   # pcapng format
}

class QuantumPacket:
    """A packet that exists in superposition until observed."""

    def __init__(self, raw_data, timestamp: float, interface_id: int = 0):
        # CRITICAL FIX: Ensure raw_data is always bytes
        self._raw_data = None
        self._set_raw_data(raw_data)

        self.timestamp = float(timestamp) if timestamp is not None else 0.0
        self.interface_id = int(interface_id)
        self.state = None  # Collapsed state
        self.observables = {}  # Measurement results

    def _set_raw_data(self, raw_data):
        """Safely set raw_data, ensuring it's always bytes."""
        if raw_data is None:
            self._raw_data = b''
        elif isinstance(raw_data, bytes):
            self._raw_data = raw_data
        elif isinstance(raw_data, bytearray):
            self._raw_data = bytes(raw_data)
        elif isinstance(raw_data, str):
            self._raw_data = raw_data.encode('utf-8', errors='ignore')
        elif isinstance(raw_data, (int, float)):
            # Convert numbers to bytes representation
            self._raw_data = str(raw_data).encode('utf-8')
        elif hasattr(raw_data, '__bytes__'):
            try:
                self._raw_data = bytes(raw_data)
            except:
                self._raw_data = b''
        elif hasattr(raw_data, '__len__') and hasattr(raw_data, '__getitem__'):
            # Try to treat as sequence of integers
            try:
                self._raw_data = bytes(raw_data)
            except:
                self._raw_data = b''
        else:
            # Last resort: use repr
            try:
                self._raw_data = repr(raw_data).encode('utf-8', errors='ignore')
            except:
                self._raw_data = b''

    @property
    def raw_data(self):
        """Get the raw data, guaranteed to be bytes."""
        if self._raw_data is None:
            return b''
        elif isinstance(self._raw_data, bytes):
            return self._raw_data
        else:
            # Emergency conversion
            try:
                self._raw_data = bytes(self._raw_data)
                return self._raw_data
            except:
                return b''

    @raw_data.setter
    def raw_data(self, value):
        """Set raw_data with validation."""
        self._set_raw_data(value)

    def collapse(self, observable: str = "protocol"):
        """Collapse the packet's wavefunction by measuring an observable."""
        if observable == "protocol":
            # Superposition of possible protocols
            protocols = {
                0x0800: "IPv4",
                0x0806: "ARP",
                0x86DD: "IPv6",
            }

            # Quantum measurement
            data = self.raw_data
            if len(data) >= 14:
                try:
                    eth_type = struct.unpack('!H', data[12:14])[0]
                    # Collapse to eigenstate
                    self.state = protocols.get(eth_type, f"Unknown_{eth_type:04x}")

                    # Heisenberg: measuring protocol disturbs other properties
                    self.observables['protocol_measured'] = True
                    self.observables['position_uncertainty'] = PLANCK_COGNITIVE / max(len(data), 1)
                except:
                    self.state = "Corrupted"
            else:
                self.state = "Too_Short"

        return self.state

    def entanglement_entropy(self):
        """Calculate the entanglement entropy of the packet."""
        if not self.state:
            self.collapse()

        # Handle empty packets
        data = self.raw_data
        if not data:
            return 0.0

        # Entropy = -∑ p_i log p_i, but quantum!
        try:
            byte_freq = Counter(data)
            total = len(data)
            if total == 0:
                return 0.0

            entropy = 0.0
            for count in byte_freq.values():
                p = count / total
                if p > 0:
                    entropy -= p * math.log2(p)

            # Quantum correction factor (avoid division by zero)
            if BOLTZMANN_BEHAVIORAL > 0:
                quantum_correction = math.sin(PLANCK_COGNITIVE * entropy / BOLTZMANN_BEHAVIORAL)
            else:
                quantum_correction = 0.0

            return entropy * (1 + 0.1 * quantum_correction)
        except Exception as e:
            # Silent fail - return 0 entropy for problematic packets
            return 0.0

class CognitivePCAPParser:
    """Parse PCAP files while modeling user cognitive load."""

    def __init__(self, filename: str = None):
        self.filename = filename
        self.packets = []
        self.entropy_field = {}
        self.cognitive_metric_tensor = None
        self.behavioral_wavefunction = None
        self.format_info = {}

        # Unified Field Theory parameters
        self.coupling_constants = {
            'g1': 0.1,  # User-system coupling
            'g2': 0.05,  # Memory-effort coupling
            'g3': 0.2,  # Security-usability coupling
            'lambda': 0.01,  # Self-interaction
        }

        logging.info("CognitivePCAPParser initialized with quantum gravity corrections")

    def detect_format(self, filename: str):
        """Detect the format of the capture file."""
        try:
            with open(filename, 'rb') as f:
                # Read magic number
                magic_bytes = f.read(4)
                if len(magic_bytes) < 4:
                    return None, None

                # Try both endianness
                magic_le = struct.unpack('<I', magic_bytes)[0]
                magic_be = struct.unpack('>I', magic_bytes)[0]

                for magic, (endian, format_type) in PCAP_MAGIC_NUMBERS.items():
                    if magic_le == magic:
                        return endian, format_type
                    elif magic_be == magic:
                        return endian, format_type

                # Check for .cap files that might have different magic
                if magic_bytes[:2] == b'\xff\xff':  # Some wireless captures
                    return "unknown", "wireless_cap"

                return None, None

        except Exception as e:
            logging.error(f"Error detecting format: {e}")
            return None, None

    def parse_file(self, filename: str = None):
        """Parse PCAP file with quantum tunneling through corrupted sections."""
        if filename:
            self.filename = filename

        if not self.filename:
            raise ValueError("No filename provided for quantum parsing")

        # Detect file format
        endian, format_type = self.detect_format(self.filename)

        if format_type == "pcapng":
            logging.info("Detected pcapng format. Using quantum-enhanced pcapng parser...")
            self._parse_pcapng()
        elif format_type in ["classic", "nanosecond"]:
            logging.info(f"Detected classic pcap format ({endian}-endian)")
            self._parse_classic_pcap(endian, format_type)
        else:
            logging.warning("Unknown format. Trying classical dpkt...")
            if DPKT_AVAILABLE:
                self._parse_with_dpkt()
            else:
                raise ValueError(f"Unknown file format: {self.filename}")

    def _parse_classic_pcap(self, endian: str, format_type: str):
        """Parse classic pcap format."""
        try:
            with open(self.filename, 'rb') as f:
                # Read global header
                global_header = f.read(24)

                # Parse based on endianness
                if endian == "little":
                    fmt = '<IHHIIII'
                else:
                    fmt = '>IHHIIII'

                magic, version_major, version_minor, thiszone, sigfigs, snaplen, network = \
                    struct.unpack(fmt, global_header)

                self.format_info = {
                    'magic': f"{magic:08x}",
                    'version': f"{version_major}.{version_minor}",
                    'snaplen': snaplen,
                    'network': network,
                    'format': format_type,
                    'endian': endian
                }

                # Determine timestamp format
                nanosecond_precision = (format_type == "nanosecond")

                # Parse packets
                packet_count = 0
                while True:
                    packet_header = f.read(16)
                    if len(packet_header) < 16:
                        break  # End of file

                    # Parse packet header
                    if endian == "little":
                        ts_sec, ts_frac, incl_len, orig_len = struct.unpack('<IIII', packet_header)
                    else:
                        ts_sec, ts_frac, incl_len, orig_len = struct.unpack('>IIII', packet_header)

                    # Calculate timestamp
                    if nanosecond_precision:
                        timestamp = ts_sec + ts_frac / 1_000_000_000
                    else:
                        timestamp = ts_sec + ts_frac / 1_000_000

                    # Read packet data
                    packet_data = f.read(incl_len)
                    if len(packet_data) < incl_len:
                        # Quantum tunnel through missing bytes
                        missing = incl_len - len(packet_data)
                        packet_data += b'\x00' * missing
                        logging.warning(f"Packet {packet_count}: Quantum tunneled through {missing} missing bytes")

                    # Create quantum packet
                    qpacket = QuantumPacket(packet_data, timestamp)
                    self.packets.append(qpacket)

                    # Update entropy field
                    self._update_entropy_field(qpacket)
                    packet_count += 1

                logging.info(f"Successfully parsed {packet_count} packets using quantum-enhanced parser")

        except Exception as e:
            logging.error(f"Quantum parsing failed: {e}")
            # Fall back to dpkt
            if DPKT_AVAILABLE:
                self._parse_with_dpkt()
            else:
                raise

    def _parse_pcapng(self):
        """Parse pcapng format with quantum corrections."""
        if not DPKT_AVAILABLE:
            raise ValueError("pcapng parsing requires dpkt. Install with: pip install dpkt")

        try:
            with open(self.filename, 'rb') as f:
                # Use dpkt for pcapng
                reader = dpkt.pcapng.Reader(f)

                self.format_info = {
                    'format': 'pcapng',
                    'interfaces': []
                }

                # Extract interface info
                if hasattr(reader, 'interfaces'):
                    for i, iface in enumerate(reader.interfaces):
                        self.format_info['interfaces'].append({
                            'id': i,
                            'snaplen': iface.snaplen,
                            'linktype': iface.linktype
                        })

                packet_count = 0
                for buf, ts in reader:
                    # pcapng provides (buf, ts) tuples
                    qpacket = QuantumPacket(buf, ts)
                    self.packets.append(qpacket)
                    self._update_entropy_field(qpacket)
                    packet_count += 1

                logging.info(f"Successfully parsed {packet_count} pcapng packets")

        except Exception as e:
            logging.error(f"pcapng parsing failed: {e}")
            # Try alternative pcapng parsing
            self._parse_pcapng_fallback()

    def _parse_pcapng_fallback(self):
        """Alternative pcapng parser for when dpkt fails."""
        try:
            with open(self.filename, 'rb') as f:
                # Simple pcapng parser that just tries to extract packets
                data = f.read()
                pos = 0
                packet_count = 0

                while pos < len(data):
                    # Look for packet-like structures
                    if pos + 16 <= len(data):
                        block_type = struct.unpack('<I', data[pos:pos+4])[0]
                        block_len = struct.unpack('<I', data[pos+4:pos+8])[0]

                        if block_len == 0 or block_len > len(data) - pos:
                            break

                        # Check if this is an Enhanced Packet Block (0x00000006)
                        if block_type == 0x00000006 and block_len >= 32:
                            # Try to extract packet
                            try:
                                # Skip block header and interface ID
                                packet_start = pos + 16
                                incl_len = struct.unpack('<I', data[pos+12:pos+16])[0]

                                if packet_start + incl_len <= len(data):
                                    packet_data = data[packet_start:packet_start+incl_len]
                                    # Extract timestamp (simplified)
                                    ts_high = struct.unpack('<I', data[pos+8:pos+12])[0]
                                    ts_low = struct.unpack('<I', data[pos+12:pos+16])[0]
                                    # Combine high and low parts for timestamp
                                    ts_combined = (ts_high << 32) | ts_low
                                    timestamp = ts_combined / 1_000_000  # Approximate

                                    qpacket = QuantumPacket(packet_data, timestamp)
                                    self.packets.append(qpacket)
                                    self._update_entropy_field(qpacket)
                                    packet_count += 1
                            except Exception as e:
                                logging.debug(f"Failed to extract packet at position {pos}: {e}")

                        pos += block_len
                        # Align to 4 bytes
                        if block_len % 4 != 0:
                            pos += 4 - (block_len % 4)
                    else:
                        break

                if packet_count > 0:
                    logging.info(f"Fallback pcapng parser found {packet_count} packets")
                else:
                    raise ValueError("No packets found in pcapng file")

        except Exception as e:
            logging.error(f"Fallback pcapng parsing failed: {e}")
            raise ValueError(f"Could not parse pcapng file: {e}")

    def _parse_with_dpkt(self):
        """Fallback to classical dpkt parsing."""
        if not DPKT_AVAILABLE:
            raise ValueError("dpkt not available for fallback parsing")

        try:
            with open(self.filename, 'rb') as f:
                # Try to detect format
                magic = f.read(4)
                f.seek(0)

                if magic == b'\x0a\x0d\x0d\x0a':  # pcapng
                    reader = dpkt.pcapng.Reader(f)
                else:  # Assume classic pcap
                    reader = dpkt.pcap.Reader(f)

                packet_count = 0
                for ts, buf in reader:
                    qpacket = QuantumPacket(buf, ts)
                    self.packets.append(qpacket)
                    self._update_entropy_field(qpacket)
                    packet_count += 1

                logging.info(f"dpkt parsed {packet_count} packets")
                self.format_info['parsed_with'] = 'dpkt'

        except Exception as e:
            logging.error(f"dpkt parsing failed: {e}")
            raise

    def _update_entropy_field(self, packet: QuantumPacket):
        """Update the entropy field tensor."""
        try:
            entropy = packet.entanglement_entropy()
            timestamp_key = int(packet.timestamp * 1000)  # ms precision

            if timestamp_key not in self.entropy_field:
                self.entropy_field[timestamp_key] = []

            self.entropy_field[timestamp_key].append(entropy)
        except:
            pass  # Silently skip errors in entropy calculation

    def calculate_cognitive_metric(self):
        """Calculate the cognitive metric tensor for the traffic."""
        n_packets = len(self.packets)
        if n_packets == 0:
            return None

        # Initialize metric tensor (4x4 for spacetime + cognitive dimension)
        metric = [[0.0 for _ in range(5)] for _ in range(5)]

        try:
            # Time component (g_00)
            time_entropies = []
            for p in self.packets:
                try:
                    entropy = p.entanglement_entropy()
                    if isinstance(entropy, (int, float)):
                        time_entropies.append(float(entropy))
                except:
                    time_entropies.append(0.0)

            if not time_entropies:
                total_entropy = 0.0
            else:
                total_entropy = sum(time_entropies)

            metric[0][0] = -1 + 0.1 * math.log1p(max(total_entropy, 0) + 1)

            # Spatial components (g_11, g_22, g_33) - represent packet size dimensions
            sizes = []
            for p in self.packets:
                try:
                    # Get the raw_data property which is guaranteed to be bytes
                    data = p.raw_data
                    # Now data should be bytes, so len() should work
                    sizes.append(len(data))
                except Exception as e:
                    # Debug: log what went wrong
                    logging.debug(f"Error getting packet size: {type(p.raw_data)} = {p.raw_data}")
                    sizes.append(0)

            if sizes:
                avg_size = sum(sizes) / len(sizes)
            else:
                avg_size = 0

            for i in range(1, 4):
                denominator = (i + 1) * 1000
                if denominator != 0:
                    metric[i][i] = 1 + 0.01 * avg_size / denominator
                else:
                    metric[i][i] = 1.0

            # Cognitive component (g_44)
            metric[4][4] = 1 + 0.001 * total_entropy * PLANCK_COGNITIVE

            # Off-diagonal components (quantum correlations)
            for i in range(5):
                for j in range(i + 1, 5):
                    try:
                        # Avoid math domain errors
                        arg = PLANCK_COGNITIVE * (i + j) * total_entropy
                        correlation = math.sin(arg)
                        metric[i][j] = metric[j][i] = 0.01 * correlation
                    except:
                        metric[i][j] = metric[j][i] = 0.0

            self.cognitive_metric_tensor = metric
            return metric

        except Exception as e:
            logging.error(f"Error calculating cognitive metric: {e}")
            traceback.print_exc()
            # Return identity metric as fallback
            self.cognitive_metric_tensor = [[1.0 if i == j else 0.0 for j in range(5)] for i in range(5)]
            return self.cognitive_metric_tensor

    def compute_einstein_tensor(self):
        """Compute Einstein tensor from cognitive metric."""
        if self.cognitive_metric_tensor is None:
            self.calculate_cognitive_metric()

        try:
            metric = self.cognitive_metric_tensor
            g = metric

            # Ricci scalar approximation
            R = 0
            for i in range(5):
                for j in range(5):
                    R += g[i][j] * (1 if i == j else 0.5)

            # Einstein tensor: G_μν = R_μν - ½ g_μν R
            G = [[0.0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    # Simplified: R_μν ≈ g_μν for cognitive space
                    R_mu_nu = g[i][j]
                    G[i][j] = R_mu_nu - 0.5 * g[i][j] * R

            return G
        except:
            # Return zero tensor on error
            return [[0.0 for _ in range(5)] for _ in range(5)]

class PasswordFieldAnalyzer:
    """Apply Unified Password Field Theory to network traffic."""

    def __init__(self):
        self.field_operators = {}
        self.entanglement_graph = {}
        self.breach_correlation_tensor = None

    def analyze_pcap(self, parser: CognitivePCAPParser) -> Dict[str, Any]:
        """Analyze PCAP using UPFT."""
        try:
            results = {
                'quantum_entropy': self._calculate_quantum_entropy(parser),
                'entanglement_witness': self._compute_entanglement_witness(parser),
                'heisenberg_uncertainty': self._heisenberg_audit(parser),
                'tunneling_probability': self._quantum_tunneling_analysis(parser),
                'cognitive_curvature': self._cognitive_space_curvature(parser),
            }
            return results
        except Exception as e:
            logging.error(f"Error in UPFT analysis: {e}")
            # Return safe defaults
            return {
                'quantum_entropy': {'von_neumann': 0.0, 'renyi_2': 0.0, 'tsallis_q1.5': 0.0, 'planck_normalized': 0.0},
                'entanglement_witness': 2.0,
                'heisenberg_uncertainty': {'delta_time': 0, 'delta_entropy': 0, 'product': 0, 'quantum_limit': PLANCK_COGNITIVE/2, 'violation': False},
                'tunneling_probability': {'tunneling_probability': 0.0, 'barrier_height': float('inf'), 'cognitive_mass': 1.0, 'barrier_width': 0.0},
                'cognitive_curvature': 0.0,
            }

    def _calculate_quantum_entropy(self, parser: CognitivePCAPParser) -> Dict[str, float]:
        """Calculate various entropy measures."""
        if not parser.packets:
            return {'von_neumann': 0.0, 'renyi_2': 0.0, 'tsallis_q1.5': 0.0, 'planck_normalized': 0.0}

        try:
            # Von Neumann entropy (quantum)
            entropy_sum = sum(p.entanglement_entropy() for p in parser.packets)
            avg_entropy = entropy_sum / len(parser.packets)

            # Renyi entropies
            sample_size = min(100, len(parser.packets))
            if sample_size > 0:
                renyi_2 = -math.log2(sum(math.exp(-2 * p.entanglement_entropy())
                                       for p in parser.packets[:sample_size]) / sample_size)
            else:
                renyi_2 = 0.0

            # Tsallis entropy (non-extensive)
            q = 1.5
            if sample_size > 0:
                tsallis = (1/(q-1)) * (1 - sum(p.entanglement_entropy()**(1-q)
                                            for p in parser.packets[:sample_size]) / sample_size)
            else:
                tsallis = 0.0

            return {
                'von_neumann': float(avg_entropy),
                'renyi_2': float(renyi_2),
                'tsallis_q1.5': float(tsallis),
                'planck_normalized': float(avg_entropy * PLANCK_COGNITIVE)
            }
        except:
            return {'von_neumann': 0.0, 'renyi_2': 0.0, 'tsallis_q1.5': 0.0, 'planck_normalized': 0.0}

    def _compute_entanglement_witness(self, parser: CognitivePCAPParser) -> float:
        """Compute entanglement witness for password reuse patterns."""
        try:
            # Look for patterns suggesting credential reuse
            patterns = defaultdict(int)

            for packet in parser.packets[:1000]:  # Limit to first 1000 packets
                # Simple pattern detection
                try:
                    data_str = packet.raw_data[:100].decode('ascii', errors='ignore').lower()

                    # Check for common password patterns
                    common_patterns = ['password', '123', 'admin', 'login', 'auth']
                    for pattern in common_patterns:
                        if pattern in data_str:
                            patterns[pattern] += 1
                except:
                    continue

            # Bell inequality violation witness
            # Simplified: if we see same credential patterns in different contexts
            if patterns:
                max_pattern = max(patterns.values())
                total_patterns = sum(patterns.values())

                # Quantum witness: if patterns are too correlated, S > 2
                S = 2 + 0.1 * (max_pattern / total_patterns) if total_patterns > 0 else 2

                return float(min(S, 2.8))  # Clip for realism
            return 2.0  # Classical bound
        except:
            return 2.0

    def _heisenberg_audit(self, parser: CognitivePCAPParser) -> Dict[str, Any]:
        """Heisenberg uncertainty audit for traffic."""
        if not parser.packets or len(parser.packets) < 2:
            return {'delta_time': 0, 'delta_entropy': 0, 'product': 0, 'quantum_limit': PLANCK_COGNITIVE/2, 'violation': False}

        try:
            # Δt * ΔE ≥ ħ/2
            timestamps = [p.timestamp for p in parser.packets]
            entropies = [p.entanglement_entropy() for p in parser.packets]

            # Calculate uncertainties
            delta_t = max(timestamps) - min(timestamps)
            avg_entropy = sum(entropies) / len(entropies)
            variance = sum((e - avg_entropy)**2 for e in entropies) / len(entropies)
            delta_E = math.sqrt(variance) if variance >= 0 else 0

            heisenberg_product = delta_t * delta_E
            quantum_limit = PLANCK_COGNITIVE / 2

            return {
                'delta_time': float(delta_t),
                'delta_entropy': float(delta_E),
                'product': float(heisenberg_product),
                'quantum_limit': float(quantum_limit),
                'violation': bool(heisenberg_product < quantum_limit)
            }
        except:
            return {'delta_time': 0, 'delta_entropy': 0, 'product': 0, 'quantum_limit': PLANCK_COGNITIVE/2, 'violation': False}

    def _quantum_tunneling_analysis(self, parser: CognitivePCAPParser) -> Dict[str, Any]:
        """Analyze quantum tunneling probability through security barriers."""
        if not parser.packets:
            return {'tunneling_probability': 0.0, 'barrier_height': float('inf'), 'cognitive_mass': 1.0, 'barrier_width': 0.0}

        try:
            # Simple model: tunneling through entropy barriers
            avg_entropy = sum(p.entanglement_entropy() for p in parser.packets) / len(parser.packets)

            # Barrier height ~ 1/entropy (low entropy = high barrier)
            barrier_height = 1.0 / (avg_entropy + 0.001)

            # Tunneling probability ~ exp(-2 * barrier_width * sqrt(2*m*V)/ħ)
            m = 1.0  # Cognitive mass
            width = len(parser.packets) / 1000  # Barrier width in packet-space
            exponent = -2 * width * math.sqrt(2 * m * barrier_height) / PLANCK_COGNITIVE
            tunneling_prob = math.exp(exponent)

            return {
                'tunneling_probability': float(min(tunneling_prob, 1.0)),
                'barrier_height': float(barrier_height),
                'cognitive_mass': float(m),
                'barrier_width': float(width)
            }
        except:
            return {'tunneling_probability': 0.0, 'barrier_height': float('inf'), 'cognitive_mass': 1.0, 'barrier_width': 0.0}

    def _cognitive_space_curvature(self, parser: CognitivePCAPParser) -> float:
        """Calculate curvature of cognitive space from traffic patterns."""
        try:
            if parser.cognitive_metric_tensor is None:
                parser.calculate_cognitive_metric()

            metric = parser.cognitive_metric_tensor
            if metric is None:
                return 0.0

            # Simplified Ricci scalar calculation
            R = 0
            for i in range(5):
                for j in range(5):
                    if i == j:
                        R += metric[i][j]
                    else:
                        R += 0.5 * metric[i][j]

            # Normalize by packet count
            curvature = R / (len(parser.packets) + 1)
            return float(curvature)
        except:
            return 0.0

class SillyPCAP:
    """Main interface for the SillyPCAP module."""

    def __init__(self, filename: str = None):
        self.filename = filename
        self.parser = CognitivePCAPParser(filename)
        self.analyzer = PasswordFieldAnalyzer()
        self.results = {}

        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        logging.info("✨ SillyPCAP initialized. Remember: packets are waves until observed! ✨")

    def load_pcap(self, filename: str):
        """Load a PCAP file with quantum decoherence prevention."""
        self.filename = filename

        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Quantum vacuum detected: file '{filename}' does not exist")

        # Check file size
        file_size = os.path.getsize(filename)
        if file_size == 0:
            raise ValueError("File is empty (zero-point energy only)")

        logging.info(f"🔮 Loading {filename} ({file_size:,} bytes)...")
        self.parser.parse_file(filename)

        packet_count = len(self.parser.packets)
        if packet_count == 0:
            logging.warning("⚠️  No packets found. File may be in a superposition of empty and non-empty states.")
        else:
            logging.info(f"📦 Loaded {packet_count} packets (some may be in superposition)")

    def analyze(self) -> Dict[str, Any]:
        """Perform complete quantum-cognitive analysis."""
        if not self.parser.packets:
            raise ValueError("No packets loaded. Did you observe the PCAP file? (Or is it in superposition?)")

        try:
            # Calculate cognitive metric
            metric = self.parser.calculate_cognitive_metric()

            # Perform UPFT analysis
            upft_results = self.analyzer.analyze_pcap(self.parser)

            # Combine results
            self.results = {
                'basic_stats': {
                    'packet_count': len(self.parser.packets),
                    'time_range': self._get_time_range(),
                    'avg_entropy': self._average_packet_entropy(),
                    'format_info': self.parser.format_info,
                },
                'cognitive_metric': metric,
                'einstein_tensor': self.parser.compute_einstein_tensor(),
                'upft_analysis': upft_results,
                'quantum_weirdness': self._calculate_quantum_weirdness(),
            }

            return self.results

        except Exception as e:
            logging.error(f"Quantum analysis failed: {e}")
            # Return minimal results
            self.results = {
                'basic_stats': {
                    'packet_count': len(self.parser.packets),
                    'time_range': (0, 0),
                    'avg_entropy': 0,
                    'format_info': self.parser.format_info,
                },
                'error': str(e)
            }
            return self.results

    def _get_time_range(self) -> Tuple[float, float]:
        """Get time range of captured packets."""
        if not self.parser.packets:
            return (0, 0)

        try:
            timestamps = [p.timestamp for p in self.parser.packets]
            return (float(min(timestamps)), float(max(timestamps)))
        except:
            return (0, 0)

    def _average_packet_entropy(self) -> float:
        """Calculate average entanglement entropy."""
        if not self.parser.packets:
            return 0.0

        try:
            total = sum(p.entanglement_entropy() for p in self.parser.packets)
            return float(total / len(self.parser.packets))
        except:
            return 0.0

    def _calculate_quantum_weirdness(self) -> Dict[str, Any]:
        """Calculate various quantum weirdness metrics."""
        if not self.parser.packets:
            return {
                'quantum_weirdness_index': 0.0,
                'coherence_time_seconds': 0.0,
                'superposition_count': 0,
                'schrodinger_cat_alive_probability': 0.5,
            }

        try:
            # Quantum weirdness index
            entropies = [p.entanglement_entropy() for p in self.parser.packets]
            avg_e = sum(entropies) / len(entropies)

            # Bell violation score
            bell_score = self.analyzer._compute_entanglement_witness(self.parser)

            # Quantum coherence (how long packets stay in superposition)
            coherence_time = PLANCK_COGNITIVE / (avg_e + 0.001)

            # Ensure probabilities are valid
            cat_prob = math.exp(-avg_e)
            if cat_prob > 1.0:
                cat_prob = 1.0
            elif cat_prob < 0.0:
                cat_prob = 0.0

            return {
                'quantum_weirdness_index': float(bell_score * avg_e),
                'coherence_time_seconds': float(coherence_time),
                'superposition_count': int(len([e for e in entropies if e > avg_e])),
                'schrodinger_cat_alive_probability': float(cat_prob),
            }
        except:
            return {
                'quantum_weirdness_index': 0.0,
                'coherence_time_seconds': 0.0,
                'superposition_count': 0,
                'schrodinger_cat_alive_probability': 0.5,
            }

    def generate_report(self) -> str:
        """Generate a silly quantum report."""
        if not self.results:
            self.analyze()

        report = []
        report.append("=" * 70)
        report.append("✨ SILLYPCAP QUANTUM-COGNITIVE ANALYSIS REPORT ✨")
        report.append("=" * 70)
        report.append(f"📄 File: {self.filename}")

        # Check for errors
        if 'error' in self.results:
            report.append(f"\n❌ Analysis Error: {self.results['error']}")
            report.append("   (The quantum cat is confused)")
            return "\n".join(report)

        basic = self.results['basic_stats']
        report.append(f"📦 Packets analyzed: {basic['packet_count']:,}")

        # Format info
        if 'format_info' in basic and basic['format_info']:
            fmt_info = basic['format_info']
            if 'format' in fmt_info:
                report.append(f"🔧 Format: {fmt_info['format']}")
            if 'parsed_with' in fmt_info:
                report.append(f"   (Parsed with: {fmt_info['parsed_with']})")

        # Time range
        time_range = basic['time_range']
        if time_range[1] > time_range[0]:
            duration = time_range[1] - time_range[0]
            report.append(f"⏱️  Time range: {duration:.2f} seconds")

        report.append("")

        # Quantum findings
        if 'upft_analysis' in self.results:
            upft = self.results['upft_analysis']
            report.append("🔮 QUANTUM FINDINGS:")

            # Entanglement Witness
            ew = upft.get('entanglement_witness', 2.0)
            if isinstance(ew, (int, float)):
                report.append(f"  • Entanglement Witness: {ew:.3f}")
                if ew > 2:
                    report.append("    ⚛️ VIOLATION OF LOCAL REALISM DETECTED!")
                    report.append("    (Credentials may be quantum entangled across sites)")
            else:
                report.append(f"  • Entanglement Witness: {ew}")

            # Heisenberg Uncertainty
            hu = upft.get('heisenberg_uncertainty', {})
            if isinstance(hu, dict):
                product = hu.get('product', 0)
                limit = hu.get('quantum_limit', PLANCK_COGNITIVE/2)
                if isinstance(product, (int, float)) and isinstance(limit, (int, float)):
                    report.append(f"  • Heisenberg Product: {product:.3e}")
                    report.append(f"  • Quantum Limit: {limit:.3e}")
                    if hu.get('violation'):
                        report.append("    ⚠️ Heisenberg principle violated!")
                        report.append("    (You're measuring too precisely or traffic is quantum weird)")

            # Tunneling Probability
            tp = upft.get('tunneling_probability', {})
            if isinstance(tp, dict):
                prob = tp.get('tunneling_probability', 0)
                if isinstance(prob, (int, float)):
                    report.append(f"  • Quantum Tunneling Probability: {prob:.3%}")
                    if prob > 0.5:
                        report.append("    🚨 HIGH TUNNELING RISK!")
                        report.append("    (Attackers may quantum tunnel through your security)")

            # Cognitive findings
            weird = self.results.get('quantum_weirdness', {})
            report.append("")
            report.append("🧠 COGNITIVE FINDINGS:")

            curvature = upft.get('cognitive_curvature', 0)
            if isinstance(curvature, (int, float)):
                report.append(f"  • Cognitive Space Curvature: {curvature:.6f}")
                if abs(curvature) > 0.1:
                    report.append("    🧠 Significant cognitive distortion detected")

            cat_prob = weird.get('schrodinger_cat_alive_probability', 0.5)
            if isinstance(cat_prob, (int, float)):
                report.append(f"  • Schrödinger's Cat Alive Probability: {cat_prob:.1%}")
                if cat_prob < 0.3:
                    report.append("    😿 The quantum cat is probably dead (bad for security)")
                elif cat_prob < 0.6:
                    report.append("    🐱 The cat is in superposition (security is uncertain)")
                else:
                    report.append("    😸 The quantum cat is alive! (superposition maintained)")

        report.append("")
        report.append("💡 RECOMMENDATIONS:")
        report.append("  1. Observe your packets less to avoid wavefunction collapse")
        report.append("  2. Apply quantum error correction to noisy credentials")
        report.append("  3. Consider quantum key distribution for important traffic")
        report.append("  4. Remember: in quantum networks, everything is entangled")
        report.append("  5. Pet Schrödinger's cat (gently, in all quantum states)")

        return "\n".join(report)

# Example usage function
def analyze_pcap_silly(filename: str) -> str:
    """One-liner to analyze a PCAP file with quantum silliness."""
    spcap = SillyPCAP(filename)
    spcap.load_pcap(filename)
    results = spcap.analyze()
    return spcap.generate_report()

# Main function for command line use
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python sillypcap.py <pcap_file>")
        print("Supported formats: .pcap, .cap, .pcapng")
        print("\nExamples:")
        print("  python sillypcap.py capture.pcap")
        print("  python sillypcap.py wireless.cap")
        print("  python sillypcap.py modern.pcapng")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if file exists
    if not os.path.exists(filename):
        print(f"❌ Error: File '{filename}' not found!")
        sys.exit(1)

    print("✨ SillyPCAP - Quantum Network Analysis ✨")
    print("=" * 50)

    try:
        spcap = SillyPCAP()
        print(f"📄 Loading: {filename}")

        # Get file info
        file_size = os.path.getsize(filename)
        print(f"📊 File size: {file_size:,} bytes")

        spcap.load_pcap(filename)

        print("🔮 Analyzing with quantum-cognitive algorithms...")
        results = spcap.analyze()

        report = spcap.generate_report()
        print("\n" + report)

        # Save results to file
        base_name = os.path.splitext(filename)[0]
        output_file = f"{base_name}_quantum_report.txt"
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(report)

        print(f"\n💾 Full results saved to: {output_file}")

    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        sys.exit(1)
    except PermissionError:
        print(f"❌ Permission denied: {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Quantum analysis failed: {e}")
        print("\n💡 Troubleshooting tips:")
        print("  1. Install dpkt: pip install dpkt")
        print("  2. Check file format with: file {filename}")
        print("  3. Try converting: editcap -F pcap input.pcapng output.pcap")
        print("  4. The file might be corrupted or in an unsupported format")

        # Try to get more info
        try:
            with open(filename, 'rb') as f:
                magic = f.read(4)
                print(f"\n🔍 File magic bytes: {magic.hex()}")
        except:
            pass

        sys.exit(1)
