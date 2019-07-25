---
category: distributed_architecture
---

<https://www.tutorialspoint.com/software_architecture_design/distributed_architecture>
1. distributed architecture의 기본은 transparency, reliability, availability다.
2. transparency - access, location, technology, migration/relocation, replication, concurrency, failure, persistence. 단어와 달리 이 아이템들을 감춰야 한다는 거다.
3. transparency 할 때 장점 - Resource sharing, openness, concurrency, scalability, fault tolerance.
4. transparency할 때 단점 - complexity, security, manageability, unpredictability.
5. Client - server architecture:
client - request 를 발급
server - request를 받고 이를 수행해서 결과를 client에게 보냄
이 과정은 서비스의 세트로 모델링 되며, 서버는 클라이언트에 대해 알 필요가 없지만, 클라이언트는 서버를 알아야 함. processers : pocesses 는 1:1이 아닐 수 있음.
6. Thin-client model : 말 그대로 클라이언트의 역할을 최소화 하는 거. legacy system을 client-server로 migration할 때 사용됨.단점은 server랑 network의 work load가 많다는 거.
7. Thick / Fat-client model: 6이랑 반대. client가 어지간한건 다 하고 server는 data management 만. client의 system이 뭔지 알 수 있는 신규 client-server system에 적합하며, 6에 비해 복잡함. 새 버전이 나올 때 마다 모든 client에 다시 설치되어야 함.
장점은 responsibility 가 separation 된 다는 거. server의 각 요소를 재사용 하기도 좋고, concurrency에도 좋음. 설계와 개발이 간단함. 기존의 어플리케이션을 분산 환경에 쉽게 migrate하거나 integrate할 수 있음. client가 많을 때 서버 자원을 효율적으로 사용할 수 있음.
8. Multi-tier Architecture: 물리적으로 분리된 Layer 를 둬서 아키텍처를 잡는 거. layer를 추가하거나 제거하기 쉬움(flexibility, reusability) .
    - 일반적인 예는 3-tier를 사용하는 거고, 이 경우 presentation, application, data storage tier를 사용.
    - presentation: 사용자의 입력을 받고 사용자에게 결과를 보여주는 레이어
    - application: command를 수행하고, 결정을 하고, 연산을 수행. 수행 내용에 따라 application의 functionality를 조절할 수 있음.
    - data: database/filesystem에 정보를 저장하거나 찾음. application에 사용될 수 있게 전달되거나, user에게 보내짐. application tier에 저장된 데이터를 관리할 수 있는 API를 제공.
장점은 thin-client보다 Better performance , thick-client 보다 쉬운 관리. reusability와 scalability의 증가. multi-threading을 제공하고 network traffic을 줄임. maintainability와 flexibility가 증가함.
단점은 testability가 별로임. reliability and availability 에 more critical
9. Broker Architectural Style - 이건 시간이 없어서 나중에....
