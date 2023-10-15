import BranchCard from "./BranchCard";
import { Progress,  Rate, Card, Row, Col } from "antd";

import axios from "axios";
import { useState, useEffect } from "react";

const review_colors = { "0%": "#b50b02", "50%": "#c2b41b", "100%": "#008c0e" };

const Home: React.FC = () => {

    interface HomePageData {
        brand_name: string;
        rating_actual: number;
        rating_rounded: number;
        rating_count:number;
        polarity_score: number;
        subjectivity_score: number;
        ratings:{
            platform_name:string;
            rating_actual: number;
            rating_rounded: number;
        }[]
        branch_ids:number[]
      }


    const [brand, setBrand] = useState<HomePageData>();
    const apiUrl = `http://157.230.114.105:8000/brand/1`;

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make the GET request using Axios
        const response = await axios.get(apiUrl);

        // Handle the response as needed
        setBrand(response.data);
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
    <>
      <div >
        <Card style={{ width: "100%" }}>
          <Row>
            <div>
              <h1>{brand?.brand_name}</h1>
            </div>
          </Row>
          <Row>
            <Col span={6}>
              <h1>{brand?.rating_actual}</h1>
              <Rate value={brand?.rating_rounded} allowHalf={true} disabled={true} />
              <h3>{brand?.rating_count}</h3>
            </Col>
            <Col span={6}>
              <Progress
                type="dashboard"
                percent={brand?.polarity_score}
                strokeColor={review_colors}
                status={"active"}
              />

              <h3>Positivity Score</h3>


            </Col>
            <Col span={6}>
            {brand?.ratings.map((rating, index) => (
                <div key={index}>
                  <h3>
                    {rating.platform_name} {rating.rating_actual}
                  </h3>
                  <Rate
                    value={rating.rating_rounded}
                    allowHalf={true}
                    disabled={true}
                  />
                </div>))}

              </Col>
            <Col span={6}>
              <h3>Subjectivity Score</h3>
              <Progress
                percent={brand?.subjectivity_score}
                status="active"
                showInfo={false}
                strokeColor={{ from: "#108ee9", to: "#87d068" }}
              />
              <h4>Objective             Subjective                 </h4>
            </Col>
          </Row>
        </Card>
      </div>
      <div>

      {brand?.branch_ids.map((ids, index) => (
                <div key={index}>
                  <BranchCard branch_id={ids}/>
                </div>))}
      </div>
    </>
  );
};

export default Home;
