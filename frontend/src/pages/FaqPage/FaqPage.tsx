import { ReactElement, useEffect, useState } from 'react';
import api from '../../utils/api/Api';
import styled from 'styled-components';
import SearchFrom from '../../components/SearchFrom/SearchFrom';
import { IFaq } from '../../utils/interfaces/interfaces';
import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Button,
} from '@mui/material';
import arrowIcon from '../../images/icons_png/arrow-down.png';

const Title = styled.h1`
  font-size: 24;
  font-weight: 600;
  text-align: left;
`;

const Subtitle = styled.p`
  margin: 0;
  padding-block: 20px;
  font-size: 16px;
  font-weight: 400;
`;

const ContentWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 20px;
`;
const CategoryWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 16px;
  text-align: left;
`;
const CategoryTitle = styled.h2`
  margin: 0;
  text-align: left;
  font-size: 20px;
  font-weight: 600;
`;

const Question = styled(AccordionSummary)`
  && {
    padding-inline: 12px;
  }
  font-size: 16px;
  font-weight: 600;

  && .MuiAccordionSummary-content {
    ::before {
      height: 0;
    }
  }
`;

const Answer = styled(AccordionDetails)`
  && {
    padding-inline: 12px;
    padding-right: 30px;
  }
  font-size: 16px;
  font-weight: 400;
`;

const ButtonWraper = styled.div`
  display: flex;
  justify-content: center;
  gap: 40px;
`;

const StyledButton = styled(Button)`
  && {
    width: 56px;
    height: 40px;
    border-radius: 100px;
  }
`;

export default function FaqPage(): ReactElement {
  const [faqList, setFaqList] = useState([] as IFaq[]);

  useEffect(() => {
    api
      .getFaq()
      .then((res: IFaq[]) => setFaqList(res))
      .catch(console.error);
  }, []);

  const category1 = faqList.filter(
    (item) => item.topic_question === 'Подключение подписки'
  );
  const category2 = faqList.filter(
    (item) => item.topic_question === 'Оформление подписки'
  );
  const category3 = faqList.filter(
    (item) => item.topic_question === 'Работа с подпиской'
  );

  return (
    <section>
      <Title>Частые вопросы</Title>
      <SearchFrom />
      <Subtitle>
        Информация о работе сервиса
        <br /> и о разделе помощи
      </Subtitle>
      <ContentWrapper>
        <CategoryWrapper>
          {' '}
          <CategoryTitle>Подключение подписки</CategoryTitle>
          {category1.map((item, index) => (
            <Accordion key={`question-${index}`}>
              <Question
                expandIcon={<img style={{ width: '24px' }} src={arrowIcon} />}
              >
                {item.question}
              </Question>
              <Answer>{item.answer}</Answer>
            </Accordion>
          ))}
        </CategoryWrapper>
        <CategoryWrapper>
          {' '}
          <CategoryTitle>Оформление подписки</CategoryTitle>
          {category2.map((item, index) => (
            <Accordion key={`question-${index}`}>
              <Question
                expandIcon={<img style={{ width: '24px' }} src={arrowIcon} />}
              >
                {item.question}
              </Question>
              <Answer>{item.answer}</Answer>
            </Accordion>
          ))}
        </CategoryWrapper>
        <CategoryWrapper>
          {' '}
          <CategoryTitle>Работа с подпиской</CategoryTitle>
          {category3.map((item, index) => (
            <Accordion key={`question-${index}`}>
              <Question
                expandIcon={<img style={{ width: '24px' }} src={arrowIcon} />}
              >
                {item.question}
              </Question>
              <Answer>{item.answer}</Answer>
            </Accordion>
          ))}
        </CategoryWrapper>
      </ContentWrapper>
      <Subtitle>
        Обратитесь в службу поддержки, если не нашли нужного ответа
      </Subtitle>
      <ButtonWraper>
        <StyledButton variant="contained" title="Позвонить нам">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M21.97 18.33C21.97 18.69 21.89 19.06 21.72 19.42C21.55 19.78 21.33 20.12 21.04 20.44C20.55 20.98 20.01 21.37 19.4 21.62C18.8 21.87 18.15 22 17.45 22C16.43 22 15.34 21.76 14.19 21.27C13.04 20.78 11.89 20.12 10.75 19.29C9.6 18.45 8.51 17.52 7.47 16.49C6.44 15.45 5.51 14.36 4.68 13.22C3.86 12.08 3.2 10.94 2.72 9.81C2.24 8.67 2 7.58 2 6.54C2 5.86 2.12 5.21 2.36 4.61C2.6 4 2.98 3.44 3.51 2.94C4.15 2.31 4.85 2 5.59 2C5.87 2 6.15 2.06 6.4 2.18C6.66 2.3 6.89 2.48 7.07 2.74L9.39 6.01C9.57 6.26 9.7 6.49 9.79 6.71C9.88 6.92 9.93 7.13 9.93 7.32C9.93 7.56 9.86 7.8 9.72 8.03C9.59 8.26 9.4 8.5 9.16 8.74L8.4 9.53C8.29 9.64 8.24 9.77 8.24 9.93C8.24 10.01 8.25 10.08 8.27 10.16C8.3 10.24 8.33 10.3 8.35 10.36C8.53 10.69 8.84 11.12 9.28 11.64C9.73 12.16 10.21 12.69 10.73 13.22C11.27 13.75 11.79 14.24 12.32 14.69C12.84 15.13 13.27 15.43 13.61 15.61C13.66 15.63 13.72 15.66 13.79 15.69C13.87 15.72 13.95 15.73 14.04 15.73C14.21 15.73 14.34 15.67 14.45 15.56L15.21 14.81C15.46 14.56 15.7 14.37 15.93 14.25C16.16 14.11 16.39 14.04 16.64 14.04C16.83 14.04 17.03 14.08 17.25 14.17C17.47 14.26 17.7 14.39 17.95 14.56L21.26 16.91C21.52 17.09 21.7 17.3 21.81 17.55C21.91 17.8 21.97 18.05 21.97 18.33Z"
              stroke="white"
              strokeWidth="1.5"
              strokeMiterlimit="10"
            />
          </svg>
        </StyledButton>
        <StyledButton variant="contained" title="Написать нам">
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M17 20.5H7C4 20.5 2 19 2 15.5V8.5C2 5 4 3.5 7 3.5H17C20 3.5 22 5 22 8.5V15.5C22 19 20 20.5 17 20.5Z"
              stroke="white"
              strokeWidth="1.5"
              strokeMiterlimit="10"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <path
              d="M17 9L13.87 11.5C12.84 12.32 11.15 12.32 10.12 11.5L7 9"
              stroke="white"
              strokeWidth="1.5"
              strokeMiterlimit="10"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </StyledButton>
      </ButtonWraper>
    </section>
  );
}
