# SELF-SUFFICIENT LORAWAN GATEWAY

Porject to build a portable and self-sufficient **LoRaWAN** gateway, that can be placed anywhere, where LTE is available.

*For example at a higher place like a hill, mountain or a church tower.*

## Setup
To bring the project to life
- create a file at root level called "config.json" (a basic structure can be found below)
- adjust the parameters in "settings.py" according to your needs.

*Also have a look at the tutorial provided by pycom - [Link to the tutorial](https://bit.ly/pygate-tutorial)*


## config.json
*Important: place your gateway ID at the end of the file into the marked position (without brackets)*
```json
{
	"SX1301_conf": {
		"lorawan_public": true,
		"clksrc": 1,
		"antenna_gain": 0,
		"radio_0": {
			"enable": true,
			"type": "SX1257",
			"freq": 867500000,
			"rssi_offset": -164.0,
			"tx_enable": true,
			"tx_freq_min": 863000000,
			"tx_freq_max": 870000000
		},
		"radio_1": {
			"enable": true,
			"type": "SX1257",
			"freq": 868500000,
			"rssi_offset": -164.0,
			"tx_enable": false
		},
		"chan_multiSF_0": {
			"enable": true,
			"radio": 1,
			"if": -400000
		},
		"chan_multiSF_1": {
			"enable": true,
			"radio": 1,
			"if": -200000
		},
		"chan_multiSF_2": {
			"enable": true,
			"radio": 1,
			"if": 0
		},
		"chan_multiSF_3": {
			"enable": true,
			"radio": 0,
			"if": -400000
		},
		"chan_multiSF_4": {
			"enable": true,
			"radio": 0,
			"if": -200000
		},
		"chan_multiSF_5": {
			"enable": true,
			"radio": 0,
			"if": 0
		},
		"chan_multiSF_6": {
			"enable": true,
			"radio": 0,
			"if": 200000
		},
		"chan_multiSF_7": {
			"enable": true,
			"radio": 0,
			"if": 400000
		},
		"chan_Lora_std": {
			"enable": true,
			"radio": 1,
			"if": -200000,
			"bandwidth": 250000,
			"spread_factor": 7
		},
		"chan_FSK": {
			"enable": true,
			"radio": 1,
			"if": 300000,
			"bandwidth": 125000,
			"datarate": 50000
		},
		"tx_lut_0": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_1": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_2": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_3": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_4": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_5": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_6": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 9,
			"dig_gain": 3
		},
		"tx_lut_7": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 11,
			"dig_gain": 3
		},
		"tx_lut_8": {
			"pa_gain": 0,
			"mix_gain": 5,
			"rf_power": 13,
			"dig_gain": 2
		},
		"tx_lut_9": {
			"pa_gain": 0,
			"mix_gain": 8,
			"rf_power": 14,
			"dig_gain": 3
		},
		"tx_lut_10": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 15,
			"dig_gain": 2
		},
		"tx_lut_11": {
			"pa_gain": 0,
			"mix_gain": 6,
			"rf_power": 16,
			"dig_gain": 1
		},
		"tx_lut_12": {
			"pa_gain": 0,
			"mix_gain": 9,
			"rf_power": 17,
			"dig_gain": 3
		},
		"tx_lut_13": {
			"pa_gain": 0,
			"mix_gain": 10,
			"rf_power": 18,
			"dig_gain": 3
		},
		"tx_lut_14": {
			"pa_gain": 0,
			"mix_gain": 11,
			"rf_power": 19,
			"dig_gain": 3
		},
		"tx_lut_15": {
			"pa_gain": 0,
			"mix_gain": 12,
			"rf_power": 27,
			"dig_gain": 3
		}
	},

	"gateway_conf": {
		"gateway_ID": "{enter your gateway id here}",
		"server_address": "router.eu.thethings.network",
		"serv_port_up": 1700,
		"serv_port_down": 1700,
		"keepalive_interval": 10,
		"stat_interval": 30,
		"push_timeout_ms": 2500,
		"autoquit_threshold": 6,
		"forward_crc_valid": true,
		"forward_crc_error": false,
		"forward_crc_disabled": false
	}
}
```
*NOTE: "tx_lut_15" was adjusted to fix an error (rf_power: 20 -> rf_power: 27)*

*NOTE: The "push_timeout_ms" is very high, as it can be due to bad network that a timeout event is fired, even if the server has acknowledged the receipt*


## gateway_conf
Short description about the paramters (can be found at the end of the config.json file)

```
gateway_ID – gateway identifier sent in each message to the network server
server_address – address of the network server
serv_port_up – port for sending uplink packets to the network server
serv_port_down – port to communicate to receive downlink packet from the network server
keepalive_interval – interval to ping the network server
stat_interval – interval to send stat messages to the network server
push_timeout_ms – socket timeout when publishing messages to the network server
autoquit_threshold – number of keepalive messages without response to wait before quitting
forward_crc_valid – enable to forward valid packets to the network server, default: true
forward_crc_error – enable to forward CRC failed packets to the network server, default: true. The network server will reject packets with failed CRC, it may not be necessary to forward the packets except for a statistic of local RF quality or to monitor the gateway performance over time. Some random CRC failed packets are expected to be received from random noise.
forward_crc_disabled – enable to forward packets without CRC enabled to the network server, default: false. LoRaWAN protocol expects uplink packets to have CRC enabled.
```

## LTE signal strenght

The value from the result of the **AT+CSQ** command is mapped to the **RSSI dBm**

```json
Value   RSSI dBm    Condition

2        	-109 	Marginal        |
3 	        -107 	Marginal        |
4 	        -105 	Marginal        |
5 	        -103 	Marginal        |   red
6 	        -101 	Marginal        |
7 	        -99 	Marginal        |
8 	        -97 	Marginal        |
9 	        -95 	Marginal        |

10 	        -93 	OK              |
11 	        -91 	OK              |
12 	        -89 	OK              |   orange
13 	        -87 	OK              |
14 	        -85 	OK              |

15 	        -83 	Good            |
16 	        -81 	Good            |
17 	        -79 	Good            |   yellow
18 	        -77 	Good            |
19 	        -75 	Good            |

20 	        -73 	Excellent       |
21 	        -71 	Excellent       |
22 	        -69 	Excellent       |
23 	        -67 	Excellent       |
24 	        -65 	Excellent       |
25 	        -63 	Excellent       |   green
26 	        -61 	Excellent       |
27 	        -59 	Excellent       |
28 	        -57 	Excellent       |
29 	        -55 	Excellent       |
30 	        -53 	Excellent       |
```