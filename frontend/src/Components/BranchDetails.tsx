import { Progress, Rate, Card, Row, Col } from "antd";
import axios from "axios";
import { useEffect, useState } from "react";
import {  useParams } from "react-router-dom";

const review_colors = { "0%": "#b50b02", "50%": "#c2b41b", "100%": "#008c0e" };

const BranchDetails: React.FC = () => {
  const { id } = useParams();
  const [branchdetails, setBranchDetails] = useState<BranchDetailsData>();
  const apiUrl = `http://157.230.114.105:8000/branch/` + { id } +`./detail`;

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make the GET request using Axios
        const response = await axios.get(apiUrl);

        // Handle the response as needed
        setBranchDetails(response.data);
        console.log("Response data:", response.data);
      } catch (error) {
        // Handle any errors that occur during the request
        console.error("Error fetching data:", error);
      }
    };

    // Call the fetchData function inside the useEffect callback
    fetchData();
  }, []);

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
                strokeColor={{ from: "#108ee9", to: "#87d068" }}
              />
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
      <div >
        {branchdetails?.meals.map((meal, index) => (
          <div key={index} style={{margin:"15px"}}>
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
