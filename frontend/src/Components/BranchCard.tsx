import { Progress, Rate, Card, Row, Col } from "antd";
import axios from "axios";
import { useEffect, useState } from "react";

const review_colors = { "0%": "#b50b02", "50%": "#c2b41b", "100%": "#008c0e" };
 // Replace with your actual API endpoint

interface BranchData {
  branch_name: string;
  branch_id: number;
  polarity_score: number;
  subjectivity_score: number;
  rating_actual: number;
  rating_rounded: number;
  rating_count: number;
}

interface BranchProps {
  branch_id: number;
}

const BranchCard: React.FC<BranchProps> = ({ branch_id }) => {
  const [branch, setBranch] = useState<BranchData>();
  const apiUrl = `http://157.230.114.105:8000/branch/` + {branch_id};
  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make the GET request using Axios
        const response = await axios.get(apiUrl);

        // Handle the response as needed
        setBranch(response.data);
        console.log("Response data:", response.data);
      } catch (error) {
        // Handle any errors that occur during the request
        console.error("Error fetching data:", error);
      }
    };

    // Call the fetchData function inside the useEffect callback
    fetchData();
  }, []);
  return (
    <div  onClick={() => {
      window.location.href = `/branchdetails/${branch_id}`;
    }}

    style={{margin:"10px"}}>
    <Card
      hoverable={true}
      title={branch?.branch_name}
      style={{ width: "800px" }}
    >
      <Row>
        <Col span={8}>
          <h1>{branch?.rating_actual}</h1>
          <Rate
            value={branch?.rating_rounded}
            allowHalf={true}
            disabled={true}
          />
          <h3>{branch?.rating_count}</h3>
        </Col>
        <Col span={8}>
          <Progress
            type="dashboard"
            percent={branch?.polarity_score}
            strokeColor={review_colors}
            status={"active"}
          />
          <h3>Positivity Score</h3>
          <Row></Row>
        </Col>
        <Col span={8}>
          <h3>Subjectivity Score</h3>
          <Progress
            percent={branch?.subjectivity_score}
            status="active"
            strokeColor={{ from: "#108ee9", to: "#87d068" }}
          />
        </Col>
      </Row>
    </Card>
    </div>
  );
};

export default BranchCard;
