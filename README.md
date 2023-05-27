# Description :
This project is concerned with generation of ethernet frames restricted with specific standards and specific configurations.

# Installation :
pip install -r requirements.txt

# Run app.py :
python3 app.py
## or
python3 app.py arg1 arg2

## Notes:
1- arg1 : it is the config file , you put relative path of the file (it is recommended to be in the same folder of the project). <br>
2- arg2 : it is the output file name. <br>
3- if no arguments passed then the default values will be applied (config.ini , packets.txt). <br>
4- there is permission handler to check the ability to read from and write to the files in the args. <br>


# Report:
Report folder contains description and documentation for the project.

# Files Description:
## 1- config.ini
it contains the 3 expected configuration for each packet that is going to be generated.

### 1) Ethernet Packets Configurations :

STREAM_DURATION_MS : stream duration in milliseconds<br>
IFGs : interframe gaps<br>
SOURCE_ADDRESS : source mac address<br>
DESTINATION_ADDRESS : destination mac address<br>
ETHER_TYPE : ethernet type<br>
PAYLOAD_TYPE : payload type (can be anything)<br>
MAX_PACKET_SIZE : max packet size that can be sent without fragmentations<br>
BURST_SIZE : number of packets sent each burst<br>
BURST_PERIODICITY_US : periodicity of the burst in microseconds <br>


### 2) Ecpri Packets Configurations :

STREAM_DURATION_MS : stream duration in milliseconds<br>
IFGs : interframe gaps<br>
SOURCE_ADDRESS : source mac address<br>
DESTINATION_ADDRESS : destination mac address<br>
ETHER_TYPE : ethernet type = 0xaefe<br>
PROTOCOL_VERSION : protocol version<br>
CONCATENATION_INDICATOR : 1 bit concatenation indicator<br>
MESSAGE_TYPE : message type<br>
PAYLOAD_SIZE : size of the payload<br>
PAYLOAD_TYPE : payload type (can be anything)<br>
MAX_PACKET_SIZE : max packet size that can be sent without fragmentations<br>
BURST_SIZE : number of packets sent each burst<br>
BURST_PERIODICITY_US : periodicity of the burst in microseconds <br>
PC_ID : PC Id according to the message type<br>
SEQ_ID : sequence Id according to the message type<br>



### 3) IEEE 802.3  Configurations:
STREAM_DURATION_MS : stream duration in milliseconds<br>
IFGs : interframe gaps<br>
SOURCE_ADDRESS : source mac address<br>
DESTINATION_ADDRESS : destination mac address<br>
ETHER_TYPE : in fact it is payload size <br>
PAYLOAD_TYPE : payload type (can be anything)<br>
MAX_PACKET_SIZE : max packet size that can be sent without fragmentations<br>
BURST_SIZE : number of packets sent each burst<br>
BURST_PERIODICITY_US : periodicity of the burst in microseconds <br>


## 2- packets.txt
it is the output file that contain the packets.

## 3- app.py
root and main of the project.

# UML:
## 1- High Level Package Diagram :
![PackageUML_High_Level](https://github.com/AhmedS1ayed/Ethernet---Ecpri-Frame-Generator/assets/93644109/8953dd53-03dc-46f5-b7d2-4dd56b42e4e8)
## 2- Low Level Package Diagram :
![PackageUML generator vpd](https://github.com/AhmedS1ayed/Ethernet---Ecpri-Frame-Generator/assets/93644109/c43f1b9f-c5ea-4870-9eca-849195573fa8)
## 3- Component Diagram :
![ComponentUML_generator vpd](https://github.com/AhmedS1ayed/Ethernet---Ecpri-Frame-Generator/assets/93644109/1d0b9935-1b44-4772-b152-78de34c141da)
