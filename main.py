import consul
import pprint

c = consul.Consul(port=80)

#index, data = c.kv.get('test')

#print(bytes.decode(data.get('Value')))
#c.agent.members()
#print(c.agent.services())
pprint.pprint(c.agent.services())

