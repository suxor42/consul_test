import consul
import pprint

c = consul.Consul(port=80)

index, data = c.kv.get('test')


if data is not None:
  print(bytes.decode(data.get('Value')))
  print(index)
#c.agent.members()
#print(c.agent.services())
pprint.pprint(c.agent.services())

