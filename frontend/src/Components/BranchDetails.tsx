import { Progress, Rate, Card, Row, Col, Tooltip } from "antd";
import axios from "axios";
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { CartesianGrid, Line, LineChart, XAxis, YAxis } from "recharts";

const review_colors = { "0%": "#b50b02", "50%": "#c2b41b", "100%": "#008c0e" };

const BranchDetails: React.FC = () => {
  const { id } = useParams();
  const [chartData, setChartData] = useState<any[]>();
  const [finalChart, setFinalChart] = useState<ChartDataItem[]>();

  

  const apiUrl = `http://157.230.114.105:8000/branch/1/detail`;
 
  const chartUrl = `http://157.230.114.105:8000/branch/1/chart`;
  const [branchdetails, setBranchDetails] = useState<BranchDetailsData | null>(null);

  useEffect(() => {
    const apiUrl = `http://157.230.114.105:8000/branch/${id}/detail`;
    const chartUrl = `http://157.230.114.105:8000/branch/${id}/chart`;

    const fetchData = async () => {
      try {
        const responseDetails = await axios.get(apiUrl);
        setBranchDetails(responseDetails.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [id]);

  type ChartDataItem = {
    date: string;
    rating: number;
  };

  interface BranchDetailsData {
    branch_name: string;
    // Other properties
    ratings_chart: number[];
  }

  const dataWithIndex = (branchdetails?.ratings_chart || []).map((rating, index) => ({
    date: new Date().toISOString(), // Replace with actual date
    rating: rating,
  }));

  

 
  

  interface BranchDetailsData {
    branch_name: string;
    branch_id: number;
    polarity_score: number;
    subjectivity_score: number;
    ratings: {
      platform_name: string;
      rating_actual: number;
      rating_rounded: number;
    }[];
    meals: {
      meal_name: string;
      rating_actual: number;
      rating_rounded: number;
    }[];
    ratings_chart:number[]
  }

  


  

  return (
    <>
      <div>
        <Card style={{ width: "1000px" }}>
          <Row>
            <h1>{branchdetails?.branch_name}</h1>
          </Row>
          <Row>
            <Col span={8}>
              <Progress
                type="dashboard"
                percent={branchdetails?.polarity_score}
                strokeColor={review_colors}
                status={"active"}
              />

              <h3>Positivity Score</h3>
            </Col>

            <Col span={8}>
              <h3>Subjectivity Score</h3>
              <Progress
                percent={branchdetails?.subjectivity_score}
                status="active"
                showInfo={false}
                strokeColor={{ from: "#108ee9", to: "#87d068" }}
              />
              <h4>Objective Subjective </h4>
            </Col>

            <Col span={8}>
              {branchdetails?.ratings.map((rating, index) => (
                <div key={index}>
                  <h3>
                    {rating.platform_name} {rating.rating_actual}
                  </h3>
                  <Rate
                    value={rating.rating_rounded}
                    allowHalf={true}
                    disabled={true}
                  />
                </div>
              ))}
            </Col>
          </Row>
        </Card>
      </div>
      <Card title="Recent rating change" style={{ margin: "10px" }}>
      <LineChart width={900} height={300} data={dataWithIndex}>
        <XAxis dataKey="index" />
        <YAxis ticks={[1, 2, 3, 4, 5]} domain={[1, 5]} />
        <CartesianGrid stroke="#ccc" />
        <Line type="monotone" dataKey="rating" stroke="blue" name="Unique Visitors" />
        <Tooltip />
      </LineChart>
    </Card>
      <div>
        {branchdetails?.meals.map((meal, index) => (
          <div key={index} style={{ margin: "15px" }}>
            <Card>
              <Row>
                <Col span={8}>
                  <h3>{meal.meal_name}</h3>
                </Col>
                <Col span={8}>
                  <h3>{meal.rating_actual}</h3>
                </Col>
                <Col span={8}>
                  <Rate
                    value={meal.rating_rounded}
                    allowHalf={true}
                    disabled={true}
                  />
                </Col>
              </Row>
            </Card>
          </div>
        ))}
      </div>
    </>
  );
};
export default BranchDetails;
