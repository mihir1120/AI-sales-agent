from agents.orchestrator import create_sales_graph


def test_sales_graph_routes_to_research_agent():
    graph = create_sales_graph()

    result = graph.invoke(
        {
            "requested_action": "research",
            "company_name": "Example Technologies",
        }
    )

    assert result["result"]["agent"] == "research"
    assert result["result"]["company_name"] == "Example Technologies"
    assert "orchestrator:routed" in result["messages"]
    assert "research:completed" in result["messages"]
